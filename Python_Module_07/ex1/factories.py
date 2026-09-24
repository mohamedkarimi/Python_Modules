from ex0.factory import CreatureFactory
from ex0.creature import Creature
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def creat_base(self) -> Creature:
        return Sproutling()

    def creat_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def creat_base(self) -> Creature:
        return Shiftling()

    def creat_evolved(self) -> Creature:
        return Morphagon()
