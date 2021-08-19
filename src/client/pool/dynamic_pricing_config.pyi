__all__ = [
    'DynamicPricingConfig',
]
from toloka.client.primitives.base import BaseTolokaObject
from toloka.client.util._extendable_enum import ExtendableStrEnum
from typing import (
    Any,
    Dict,
    List,
    Optional
)

class DynamicPricingConfig(BaseTolokaObject):
    """The dynamic pricing settings.

    Attributes:
        type: Parameter type for calculating dynamic pricing. The SKILL value.
        skill_id: ID of the skill that the task price is based on
        intervals: Skill level intervals. Must not overlap.
            A performer with a skill level that is not included in any interval will receive the basic
            price for a task suite.
    """

    class Interval(BaseTolokaObject):
        """Skill level interval

        Attributes:
            from_: Lower bound of the interval.
            to: dynamic_pricing_config.intervals.to
            reward_per_assignment: The price per task page for a performer with the specified skill level.
        """

        def __init__(
            self,
            *,
            from_: Optional[int] = None,
            to: Optional[int] = None,
            reward_per_assignment: Optional[float] = None
        ) -> None:
            """Method generated by attrs for class DynamicPricingConfig.Interval.
            """
            ...

        _unexpected: Optional[Dict[str, Any]]
        from_: Optional[int]
        to: Optional[int]
        reward_per_assignment: Optional[float]

    class Type(ExtendableStrEnum):
        """Dynamic pricing type
        """

        SKILL = 'SKILL'

    def __init__(
        self,
        type: Optional[Type] = None,
        skill_id: Optional[str] = None,
        intervals: Optional[List[Interval]] = None
    ) -> None:
        """Method generated by attrs for class DynamicPricingConfig.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    type: Optional[Type]
    skill_id: Optional[str]
    intervals: Optional[List[Interval]]
