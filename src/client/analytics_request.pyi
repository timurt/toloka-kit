__all__ = [
    'AnalyticsRequest',
    'PoolAnalyticsRequest',
    'RealTasksCountPoolAnalytics',
    'SubmitedAssignmentsCountPoolAnalytics',
    'SkippedAssignmentsCountPoolAnalytics',
    'RejectedAssignmentsCountPoolAnalytics',
    'ApprovedAssignmentsCountPoolAnalytics',
    'CompletionPercentagePoolAnalytics',
    'AvgSubmitAssignmentMillisPoolAnalytics',
    'SpentBudgetPoolAnalytics',
    'UniqueWorkersCountPoolAnalytics',
    'UniqueSubmittersCountPoolAnalytics',
    'ActiveWorkersByFilterCountPoolAnalytics',
    'EstimatedAssignmentsCountPoolAnalytics',
]
from toloka.client.primitives.base import BaseTolokaObject
from toloka.client.util._extendable_enum import ExtendableStrEnum
from typing import (
    Any,
    Dict,
    Optional
)

class AnalyticsRequest(BaseTolokaObject):
    """Base class for all analytics requests in Toloka

    How to use this requests and get some useful information see in example in "TolokaClient.get_analytics".

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    class Subject(ExtendableStrEnum):
        """An enumeration.
        """

        POOL = 'POOL'

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class AnalyticsRequest.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class PoolAnalyticsRequest(AnalyticsRequest):
    """Base class for all analytics requests about pools

    Right now you can get analytics only about pool.

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    class Subject(ExtendableStrEnum):
        """An enumeration.
        """

        REAL_TASKS_COUNT = 'real_tasks_count'
        SUBMITTED_ASSIGNMENTS_COUNT = 'submitted_assignments_count'
        SKIPPED_ASSIGNMENTS_COUNT = 'skipped_assignments_count'
        REJECTED_ASSIGNMENTS_COUNT = 'rejected_assignments_count'
        APPROVED_ASSIGNMENTS_COUNT = 'approved_assignments_count'
        COMPLETION_PERCENTAGE = 'completion_percentage'
        AVG_SUBMIT_ASSIGNMENT_MILLIS = 'avg_submit_assignment_millis'
        SPENT_BUDGET = 'spent_budget'
        UNIQUE_WORKERS_COUNT = 'unique_workers_count'
        UNIQUE_SUBMITTERS_COUNT = 'unique_submitters_count'
        ACTIVE_WORKERS_BY_FILTER_COUNT = 'active_workers_by_filter_count'
        ESTIMATED_ASSIGNMENTS_COUNT = 'estimated_assignments_count'

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class PoolAnalyticsRequest.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class RealTasksCountPoolAnalytics(PoolAnalyticsRequest):
    """The number of tasks in the pool

    It does not take into account the overlap, how many tasks will be on one page, or the presence of golden tasks.

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class RealTasksCountPoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class SubmitedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):
    """Number of assignments in the "submited" status in the pool

    Do not confuse it with the approved status.
    "Submited" status means that the task was completed by the performer and send for review.
    "Approved" status means that the task has passed review and money has been paid for it.

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class SubmitedAssignmentsCountPoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class SkippedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):
    """Number of assignments in the "skipped" status in the pool

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class SkippedAssignmentsCountPoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class RejectedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):
    """Number of assignments in the "rejected" status in the pool

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class RejectedAssignmentsCountPoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class ApprovedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):
    """Number of assignments in the "approved" status in the pool

    Do not confuse it with the submited status.
    "Submited" status means that the task was completed by the performer and send for review.
    "Approved" status means that the task has passed review and money has been paid for it.

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class ApprovedAssignmentsCountPoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class CompletionPercentagePoolAnalytics(PoolAnalyticsRequest):
    """Approximate percentage of completed tasks in the pool

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class CompletionPercentagePoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class AvgSubmitAssignmentMillisPoolAnalytics(PoolAnalyticsRequest):
    """Average time to complete one task page in milliseconds

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class AvgSubmitAssignmentMillisPoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class SpentBudgetPoolAnalytics(PoolAnalyticsRequest):
    """How much money has already been spent on this pool, excluding fee

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class SpentBudgetPoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class UniqueWorkersCountPoolAnalytics(PoolAnalyticsRequest):
    """The number of unique performers who took tasks from the pool

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class UniqueWorkersCountPoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class UniqueSubmittersCountPoolAnalytics(PoolAnalyticsRequest):
    """The number of unique performers who have submitted to the pool

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class UniqueSubmittersCountPoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str


class ActiveWorkersByFilterCountPoolAnalytics(PoolAnalyticsRequest):
    """The number of active performers matching the pool filters for the last hours

    Attributes:
        subject_id: ID of the object you want to get analytics about.
        interval_hours: The number of hours to take into account when collecting statistics.
    """

    def __init__(
        self,
        *,
        subject_id: str,
        interval_hours: int
    ) -> None:
        """Method generated by attrs for class ActiveWorkersByFilterCountPoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str
    interval_hours: int


class EstimatedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):
    """The approximate number of responses to task pages.

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    def __init__(self, *, subject_id: str) -> None:
        """Method generated by attrs for class EstimatedAssignmentsCountPoolAnalytics.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str
