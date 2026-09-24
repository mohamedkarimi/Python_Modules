from typing import cast

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    print("base:")
    base_heal = healing_factory.creat_base()
    heal_base = cast(HealCapability, base_heal)
    print(base_heal.describe())
    print(base_heal.attack())
    print(heal_base.heal())

    print("evolved:")
    evolved_heal = healing_factory.creat_evolved()
    heal_evolved = cast(HealCapability, evolved_heal)
    print(evolved_heal.describe())
    print(evolved_heal.attack())
    print(heal_evolved.heal())

    print()
    print("Testing Creature with transform capability")
    print("base:")
    base_transform = transform_factory.creat_base()
    transform_base = cast(TransformCapability, base_transform)
    print(base_transform.describe())
    print(base_transform.attack())
    print(transform_base.transform())
    print(base_transform.attack())
    print(transform_base.revert())

    print("evolved:")
    evolved_transform = transform_factory.creat_evolved()
    transform_evolved = cast(TransformCapability, evolved_transform)
    print(evolved_transform.describe())
    print(evolved_transform.attack())
    print(transform_evolved.transform())
    print(evolved_transform.attack())
    print(transform_evolved.revert())


if __name__ == "__main__":
    main()
