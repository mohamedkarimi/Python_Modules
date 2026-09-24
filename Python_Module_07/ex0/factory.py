from abc import ABC, abstractmethod
from .creature import Creature
from .flame import Flameling, Pyrodon
from .aqua import Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def creat_base(self) -> Creature:
        """Create and return the base creature of a family"""
        pass

    @abstractmethod
    def creat_evolved(self) -> Creature:
        """Create and return the evolved creature of family"""
        pass


class FlameFactory(CreatureFactory):
    def creat_base(self) -> Creature:
        return Flameling()

    def creat_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def creat_base(self) -> Creature:
        return Aquabub()

    def creat_evolved(self) -> Creature:
        return Torragon()
