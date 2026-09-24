#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.initial_height: float = height

    def grow(self) -> None:
        self.height += 1

    def age_one_day(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def wekly_growth(self) -> float:
        return self.height - self.initial_height


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant.get_info()

    for i in range(6):
        plant.grow()
        plant.age_one_day()
    print("=== Day 7 ===")
    plant.get_info()
    print(f"Growth this week: +{plant.wekly_growth()}cm")
