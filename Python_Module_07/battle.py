from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base_creature = factory.creat_base()
    evolved_creature = factory.creat_evolved()

    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print()


def test_battle(
        factory_one: CreatureFactory,
        factory_two: CreatureFactory,
) -> None:
    print("Testing battle")

    creature_one = factory_one.creat_base()
    creature_two = factory_two.creat_base()

    print(creature_one.describe())
    print("vs.")
    print(creature_two.describe())
    print("fight!")
    print(creature_one.attack())
    print(creature_two.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
