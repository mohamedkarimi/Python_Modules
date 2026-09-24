from abc import ABC, abstractmethod
from typing import cast

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from ex2.exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return True if the creature can use this strategy."""
        raise NotImplementedError

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Perform the strategy actions for the given creature."""
        raise NotImplementedError


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        transform_creature = cast(TransformCapability, creature)
        print(transform_creature.transform())
        print(creature.attack())
        print(transform_creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        heal_creature = cast(HealCapability, creature)
        print(creature.attack())
        print(heal_creature.heal())
