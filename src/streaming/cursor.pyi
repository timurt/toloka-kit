__all__ = [
    'AssignmentCursor',
    'BaseCursor',
    'DATETIME_MIN',
    'TaskCursor',
    'TolokaClientSyncOrAsyncType',
    'UserBonusCursor',
    'UserSkillCursor',
]
import datetime
import toloka.client
import toloka.client.assignment
import toloka.client.search_requests
import toloka.streaming.event
import toloka.util.async_utils
import typing

RequestObjectType = typing.TypeVar('RequestObjectType')
ResponseObjectType = typing.TypeVar('ResponseObjectType')
TolokaClientSyncOrAsyncType = typing.Union[toloka.client.TolokaClient, toloka.util.async_utils.AsyncMultithreadWrapper[toloka.client.TolokaClient]]

DATETIME_MIN = ...

class BaseCursor:
    class CursorFetchContext:
        """Context manager to return from `BaseCursor.try_fetch_all method`.
        Commit cursor state only if no error occured.
        """

        def __init__(self, cursor: 'BaseCursor') -> None:
            """Method generated by attrs for class BaseCursor.CursorFetchContext.
            """
            ...

        _cursor: 'BaseCursor'
        _start_state: typing.Optional[typing.Tuple]
        _finish_state: typing.Optional[typing.Tuple]

    def try_fetch_all(self) -> CursorFetchContext: ...

    def __init__(
        self,
        toloka_client: TolokaClientSyncOrAsyncType,
        request: RequestObjectType
    ) -> None:
        """Method generated by attrs for class BaseCursor.
        """
        ...

    toloka_client: TolokaClientSyncOrAsyncType
    _request: typing.Any
    _prev_response: typing.Any


class AssignmentCursor(BaseCursor):
    """Iterator over Assignment objects of seleted AssignmentEventType.

    Args:
        toloka_client: TolokaClient object that is being used to search assignments.
        request: Base request to search assignments by.
        event_type: Assignments event's type to search.

    Examples:
        Iterate over assignment acceptances events.

        >>> it = AssignmentCursor(pool_id='123', event_type='ACCEPTED', toloka_client=toloka_client)
        >>> current_events = list(it)
        >>> # ... new events may occur ...
        >>> new_events = list(it)  # Contains only new events, occured since the previous call.
        ...
    """

    @typing.overload
    def __init__(
        self,
        toloka_client: TolokaClientSyncOrAsyncType,
        event_type,
        request: toloka.client.search_requests.AssignmentSearchRequest = ...
    ) -> None:
        """Method generated by attrs for class AssignmentCursor.
        """
        ...

    @typing.overload
    def __init__(
        self,
        toloka_client: TolokaClientSyncOrAsyncType,
        event_type,
        status: typing.Union[str, toloka.client.assignment.Assignment.Status, typing.List[typing.Union[str, toloka.client.assignment.Assignment.Status]]] = None,
        task_id: typing.Optional[str] = None,
        task_suite_id: typing.Optional[str] = None,
        pool_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        created_lt: typing.Optional[datetime.datetime] = None,
        created_lte: typing.Optional[datetime.datetime] = None,
        created_gt: typing.Optional[datetime.datetime] = None,
        created_gte: typing.Optional[datetime.datetime] = None,
        submitted_lt: typing.Optional[datetime.datetime] = None,
        submitted_lte: typing.Optional[datetime.datetime] = None,
        submitted_gt: typing.Optional[datetime.datetime] = None,
        submitted_gte: typing.Optional[datetime.datetime] = None,
        accepted_lt: typing.Optional[datetime.datetime] = None,
        accepted_lte: typing.Optional[datetime.datetime] = None,
        accepted_gt: typing.Optional[datetime.datetime] = None,
        accepted_gte: typing.Optional[datetime.datetime] = None,
        rejected_lt: typing.Optional[datetime.datetime] = None,
        rejected_lte: typing.Optional[datetime.datetime] = None,
        rejected_gt: typing.Optional[datetime.datetime] = None,
        rejected_gte: typing.Optional[datetime.datetime] = None,
        skipped_lt: typing.Optional[datetime.datetime] = None,
        skipped_lte: typing.Optional[datetime.datetime] = None,
        skipped_gt: typing.Optional[datetime.datetime] = None,
        skipped_gte: typing.Optional[datetime.datetime] = None,
        expired_lt: typing.Optional[datetime.datetime] = None,
        expired_lte: typing.Optional[datetime.datetime] = None,
        expired_gt: typing.Optional[datetime.datetime] = None,
        expired_gte: typing.Optional[datetime.datetime] = None
    ) -> None:
        """Method generated by attrs for class AssignmentCursor.
        """
        ...

    toloka_client: TolokaClientSyncOrAsyncType
    _request: toloka.client.search_requests.AssignmentSearchRequest
    _prev_response: typing.Any
    _event_type: toloka.streaming.event.AssignmentEvent.Type


class TaskCursor(BaseCursor):
    """Iterator over tasks by create time.

    Args:
        toloka_client: TolokaClient object that is being used to search tasks.
        request: Base request to search tasks by.

    Examples:
        Iterate over tasks.

        >>> it = TaskCursor(pool_id='123', toloka_client=toloka_client)
        >>> current_tasks = list(it)
        >>> # ... new tasks could appear ...
        >>> new_tasks = list(it)  # Contains only new tasks, appeared since the previous call.
        ...
    """

    @typing.overload
    def __init__(
        self,
        toloka_client: TolokaClientSyncOrAsyncType,
        request: toloka.client.search_requests.TaskSearchRequest = ...
    ) -> None:
        """Method generated by attrs for class TaskCursor.
        """
        ...

    @typing.overload
    def __init__(
        self,
        toloka_client: TolokaClientSyncOrAsyncType,
        pool_id: typing.Optional[str] = None,
        overlap: typing.Optional[int] = None,
        id_lt: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        created_lt: typing.Optional[datetime.datetime] = None,
        created_lte: typing.Optional[datetime.datetime] = None,
        created_gt: typing.Optional[datetime.datetime] = None,
        created_gte: typing.Optional[datetime.datetime] = None,
        overlap_lt: typing.Optional[int] = None,
        overlap_lte: typing.Optional[int] = None,
        overlap_gt: typing.Optional[int] = None,
        overlap_gte: typing.Optional[int] = None
    ) -> None:
        """Method generated by attrs for class TaskCursor.
        """
        ...

    toloka_client: TolokaClientSyncOrAsyncType
    _request: toloka.client.search_requests.TaskSearchRequest
    _prev_response: typing.Any


class UserBonusCursor(BaseCursor):
    """Iterator over user bonuses by create time.

    Args:
        toloka_client: TolokaClient object that is being used to search user bonuses.
        request: Base request to search user bonuses by.

    Examples:
        Iterate over user bonuses.

        >>> it = UserBonusCursor(toloka_client=toloka_client)
        >>> current_bonuses = list(it)
        >>> # ... new user bonuses could appear ...
        >>> new_bonuses = list(it)  # Contains only new user bonuses, appeared since the previous call.
        ...
    """

    @typing.overload
    def __init__(
        self,
        toloka_client: TolokaClientSyncOrAsyncType,
        request: toloka.client.search_requests.UserBonusSearchRequest = ...
    ) -> None:
        """Method generated by attrs for class UserBonusCursor.
        """
        ...

    @typing.overload
    def __init__(
        self,
        toloka_client: TolokaClientSyncOrAsyncType,
        user_id: typing.Optional[str] = None,
        private_comment: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        created_lt: typing.Optional[datetime.datetime] = None,
        created_lte: typing.Optional[datetime.datetime] = None,
        created_gt: typing.Optional[datetime.datetime] = None,
        created_gte: typing.Optional[datetime.datetime] = None
    ) -> None:
        """Method generated by attrs for class UserBonusCursor.
        """
        ...

    toloka_client: TolokaClientSyncOrAsyncType
    _request: toloka.client.search_requests.UserBonusSearchRequest
    _prev_response: typing.Any


class UserSkillCursor(BaseCursor):
    """Iterator over UserSkillEvent objects of seleted event_type.

    Args:
        toloka_client: TolokaClient object that is being used to search user skills.
        request: Base request to search user skills by.
        event_type: User skill event's type to search.

    Examples:
        Iterate over user skills acceptances events.

        >>> it = UserSkillCursor(event_type='MODIFIED', toloka_client=toloka_client)
        >>> current_events = list(it)
        >>> # ... new user skills could be set ...
        >>> new_events = list(it)  # Contains only new events, occured since the previous call.
        ...
    """

    @typing.overload
    def __init__(
        self,
        toloka_client: TolokaClientSyncOrAsyncType,
        event_type,
        request: toloka.client.search_requests.UserSkillSearchRequest = ...
    ) -> None:
        """Method generated by attrs for class UserSkillCursor.
        """
        ...

    @typing.overload
    def __init__(
        self,
        toloka_client: TolokaClientSyncOrAsyncType,
        event_type,
        user_id: typing.Optional[str] = None,
        skill_id: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        created_lt: typing.Optional[datetime.datetime] = None,
        created_lte: typing.Optional[datetime.datetime] = None,
        created_gt: typing.Optional[datetime.datetime] = None,
        created_gte: typing.Optional[datetime.datetime] = None,
        modified_lt: typing.Optional[datetime.datetime] = None,
        modified_lte: typing.Optional[datetime.datetime] = None,
        modified_gt: typing.Optional[datetime.datetime] = None,
        modified_gte: typing.Optional[datetime.datetime] = None
    ) -> None:
        """Method generated by attrs for class UserSkillCursor.
        """
        ...

    toloka_client: TolokaClientSyncOrAsyncType
    _request: toloka.client.search_requests.UserSkillSearchRequest
    _prev_response: typing.Any
    _event_type: toloka.streaming.event.UserSkillEvent.Type
