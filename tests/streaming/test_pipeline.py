import asyncio
import datetime
import pytest

from toloka.client import unstructure
from toloka.util.async_utils import ComplexException, AsyncMultithreadWrapper
from toloka.streaming import AssignmentsObserver, PoolStatusObserver, Pipeline

from ..testutils.backend_mock import BackendSearchMock


@pytest.fixture
def existing_backend_assignments():
    return [
        {'pool_id': '100', 'id': 'K', 'submitted': '2020-01-01T01:01:01', 'status': 'SUBMITTED'},
        {'pool_id': '100', 'id': 'L', 'submitted': '2020-01-01T01:01:01', 'status': 'SUBMITTED'},
        {'pool_id': '100', 'id': 'M', 'submitted': '2020-01-01T01:01:01', 'status': 'SUBMITTED'},
        {'pool_id': '100', 'id': 'N', 'submitted': '2020-01-01T01:01:02', 'status': 'SUBMITTED'},
        {'pool_id': '100', 'id': 'O', 'submitted': '2020-01-01T01:01:02', 'status': 'SUBMITTED'},
        {'pool_id': '100', 'id': 'P', 'submitted': '2020-01-01T01:01:02', 'status': 'SUBMITTED'},
        {'pool_id': '100', 'id': 'B', 'submitted': '2020-01-01T01:01:03', 'status': 'SUBMITTED'},
        {'pool_id': '100', 'id': 'A', 'submitted': '2020-01-01T01:01:04', 'status': 'SUBMITTED'},
        {'pool_id': '100', 'id': 'Z', 'created': '2020-01-01T01:01:01', 'status': 'ACTIVE'},
    ]


@pytest.fixture
def new_backend_assignments():
    return [
        {'pool_id': '100', 'id': 'C', 'submitted': '2020-01-01T01:01:05', 'status': 'SUBMITTED'},
        {'pool_id': '100', 'id': 'D', 'submitted': '2020-01-01T01:01:06', 'status': 'SUBMITTED'},
    ]


def test_pipeline_errored_callback(requests_mock, toloka_url, toloka_client, existing_backend_assignments):
    storage = [item for item in existing_backend_assignments if item['status'] != 'ACTIVE']  # Make sure it stops.
    assert storage  # Check this test uses correct data.

    backend = BackendSearchMock(storage, limit=3)  # Chunk size doesn't make sense here.
    requests_mock.get(f'{toloka_url}/assignments', json=backend)
    requests_mock.get(f'{toloka_url}/pools/100', json={'id': '100', 'status': 'CLOSED'})

    class HandlerRaiseSometimes:
        def __init__(self):
            self.calls_count = 0
            self.received = []

        def __call__(self, events):
            self.calls_count += 1
            if self.calls_count % 2:
                raise ValueError('Raised from callback')
            self.received.extend(events)

    pipeline = Pipeline(datetime.timedelta(milliseconds=100))
    observer = pipeline.register(AssignmentsObserver(toloka_client, pool_id='100'))
    handler = observer.on_submitted(HandlerRaiseSometimes())

    with pytest.raises(ComplexException) as exc:
        asyncio.get_event_loop().run_until_complete(pipeline.run())
    assert 'Raised from callback' in str(exc)
    assert 1 == handler.calls_count
    assert [] == handler.received

    asyncio.get_event_loop().run_until_complete(pipeline.run())
    assert 2 == handler.calls_count
    events_expected = [{'assignment': item, 'event_type': 'SUBMITTED', 'event_time': item['submitted']}
                       for item in storage]
    assert events_expected == unstructure(handler.received)


@pytest.mark.parametrize('use_async', [False, True])
def test_pipeline(requests_mock, toloka_url, toloka_client, existing_backend_assignments, new_backend_assignments, use_async):
    pool_mock = {'id': '100', 'status': 'OPEN'}

    backend = BackendSearchMock(existing_backend_assignments, limit=3)
    requests_mock.get(f'{toloka_url}/assignments', json=backend)
    requests_mock.get(f'{toloka_url}/pools/100', json=pool_mock)

    save_submitted_here = []
    save_pool_info_here = []

    def handle_submitted(events):
        save_submitted_here.extend(event.assignment for event in events)

    async def handle_pool_open(pool):
        active_count = len(list(toloka_client.get_assignments(pool_id=pool.id, status='ACTIVE')))
        save_pool_info_here.append(f'pool open with active tasks count: {active_count}')

    class HandlePoolClose:
        async def __call__(self, pool):
            save_pool_info_here.append(f'pool closed with reason: {pool.last_close_reason.value}')

    async def _add_new_assignments(after_sec):
        await asyncio.sleep(after_sec)
        backend.storage.extend(new_backend_assignments)

    async def _expire_active_and_close_pool(after_sec):
        await asyncio.sleep(after_sec)
        for item in backend.storage:
            if item['status'] == 'ACTIVE':
                item['status'] = 'EXPIRED'
        pool_mock['status'] = 'CLOSED'
        pool_mock['last_close_reason'] = 'EXPIRED'

    _toloka_client = AsyncMultithreadWrapper(toloka_client) if use_async else toloka_client

    pipeline = Pipeline(datetime.timedelta(milliseconds=500))
    pipeline.register(AssignmentsObserver(_toloka_client, pool_id='100')).on_submitted(handle_submitted)
    pool_observer = pipeline.register(PoolStatusObserver(_toloka_client, pool_id='100'))
    pool_observer.on_open(handle_pool_open)
    pool_observer.on_closed(HandlePoolClose())

    async def _main():
        loop = asyncio.get_event_loop()
        await asyncio.wait(list(map(loop.create_task, (
            pipeline.run(),
            _add_new_assignments(after_sec=1),
            _expire_active_and_close_pool(after_sec=2),
        ))))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(_main())

    expected_saved = [item for item in backend.storage if item.get('submitted')]
    assert expected_saved == unstructure(save_submitted_here)

    assert [
        'pool open with active tasks count: 1',
        'pool closed with reason: EXPIRED',
    ] == save_pool_info_here
