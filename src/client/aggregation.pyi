"""Module for aggregating results

For example, when you need to decide whether a cat or a dog is in the picture, and you ask more than one performers.
In this case, you need to decide on the final answer and sometimes calculate the probability. This module will help you do this.
Aggregation works on the Toloka server side.

In these cases, we strongly recommend using our crowd-kit solution:
https://github.com/Toloka/crowd-kit
It will allow you to:
- use more different aggregation methods,
- perform aggregation on your side
"""

__all__ = [
    'AggregatedSolutionType',
    'PoolAggregatedSolutionRequest',
    'TaskAggregatedSolutionRequest',
    'WeightedDynamicOverlapTaskAggregatedSolutionRequest',
    'AggregatedSolution',
]
from toloka.client.primitives.base import BaseTolokaObject
from toloka.client.util._extendable_enum import ExtendableStrEnum
from typing import (
    Any,
    Dict,
    List,
    Optional
)

class AggregatedSolutionType(ExtendableStrEnum):
    """An enumeration.
    """

    WEIGHTED_DYNAMIC_OVERLAP = 'WEIGHTED_DYNAMIC_OVERLAP'
    DAWID_SKENE = 'DAWID_SKENE'


class PoolAggregatedSolutionRequest(BaseTolokaObject):
    """Request that allows you to aggregate results in a specific pool

    Responses to all completed tasks will be aggregated.
    See an example of how to use it in "TolokaClient.aggregate_solutions_by_pool".

    Attributes:
        type: Aggregation type.
            WEIGHTED_DYNAMIC_OVERLAP - Aggregation of responses in a pool with dynamic overlap.
            DAWID_SKENE - Dawid-Skene aggregation model.
                A. Philip Dawid and Allan M. Skene. 1979.
                Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm.
                Journal of the Royal Statistical Society. Series C (Applied Statistics), Vol. 28, 1 (1979), 20–28.
                https://doi.org/10.2307/2346806
        pool_id: In which pool to aggregate the results.
        answer_weight_skill_id: A skill that determines the weight of the performer's response.
        fields: Output data fields to use for aggregating responses. For best results, each of these fields
            must have a limited number of response options.
    """

    class Field(BaseTolokaObject):
        def __init__(self, *, name: Optional[str] = None) -> None:
            """Method generated by attrs for class PoolAggregatedSolutionRequest.Field.
            """
            ...

        _unexpected: Optional[Dict[str, Any]]
        name: Optional[str]

    def __init__(
        self,
        *,
        type: Optional[AggregatedSolutionType] = None,
        pool_id: Optional[str] = None,
        answer_weight_skill_id: Optional[str] = None,
        fields: Optional[List[Field]] = None
    ) -> None:
        """Method generated by attrs for class PoolAggregatedSolutionRequest.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    type: Optional[AggregatedSolutionType]
    pool_id: Optional[str]
    answer_weight_skill_id: Optional[str]
    fields: Optional[List[Field]]


class TaskAggregatedSolutionRequest(BaseTolokaObject):
    """Base class for run aggregation on a single task

    Attributes:
        task_id: Answers for which task to aggregate.
        pool_id: In which pool this task.
    """

    def __init__(
        self,
        *,
        task_id: Optional[str] = None,
        pool_id: Optional[str] = None
    ) -> None:
        """Method generated by attrs for class TaskAggregatedSolutionRequest.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    task_id: Optional[str]
    pool_id: Optional[str]


class WeightedDynamicOverlapTaskAggregatedSolutionRequest(TaskAggregatedSolutionRequest):
    """Request that allows you to run WeightedDynamicOverlap aggregation on a single task

    Attributes:
        task_id: Answers for which task to aggregate.
        pool_id: In which pool this task.
        answer_weight_skill_id: A skill that determines the weight of the performer's response.
        fields: Output data fields to use for aggregating responses. For best results, each of these fields
            must have a limited number of response options.
    """

    class Field(BaseTolokaObject):
        def __init__(self, *, name: Optional[str] = None) -> None:
            """Method generated by attrs for class WeightedDynamicOverlapTaskAggregatedSolutionRequest.Field.
            """
            ...

        _unexpected: Optional[Dict[str, Any]]
        name: Optional[str]

    def __init__(
        self,
        *,
        task_id: Optional[str] = None,
        pool_id: Optional[str] = None,
        answer_weight_skill_id: Optional[str] = None,
        fields: Optional[List[Field]] = None
    ) -> None:
        """Method generated by attrs for class WeightedDynamicOverlapTaskAggregatedSolutionRequest.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    task_id: Optional[str]
    pool_id: Optional[str]
    answer_weight_skill_id: Optional[str]
    fields: Optional[List[Field]]


class AggregatedSolution(BaseTolokaObject):
    """Aggregated response to the task

    Attributes:
        pool_id: In which pool the results were aggregated.
        task_id: The answer for which task was aggregated.
        confidence: Confidence in the aggregate response.
        output_values: Output data fields and aggregate response.
    """

    def __init__(
        self,
        *,
        pool_id: Optional[str] = None,
        task_id: Optional[str] = None,
        confidence: Optional[float] = None,
        output_values: Optional[Dict[str, Any]] = None
    ) -> None:
        """Method generated by attrs for class AggregatedSolution.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    pool_id: Optional[str]
    task_id: Optional[str]
    confidence: Optional[float]
    output_values: Optional[Dict[str, Any]]
