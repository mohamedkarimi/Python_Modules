#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        print(
            f"{self.name} (Flower): {self.height}cm,"
            f"{self.age} days, {self.color} color"
        )


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = (self.height * self.trunk_diameter) // 320
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> None:
        print(
            f"{self.name} (Tree): {self.height}cm,"
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        print(
            f"{self.name} (Vegetable): {self.height}cm,"
            f"{self.age} days, {self.harvest_season} harvest"
        )

    def show_nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    plants: list = [
        Flower("Rose", 25, 30, "red"),
        Tree("Oak", 500, 1825, 50),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
    ]

    for plant in plants:
        print()
        plant.get_info()

        if isinstance(plant, Flower):
            plant.bloom()
        elif isinstance(plant, Tree):
            plant.produce_shade()
        elif isinstance(plant, Vegetable):
            plant.show_nutrition()
