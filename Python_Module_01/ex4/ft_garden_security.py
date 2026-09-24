#!/usr/bin/env python3
class Secureplant:
    def __init__(self, name: str):
        self.name: str = name
        self.__height: float = 0
        self.__age: int = 0
        print(f"Plant created: {self.name}")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(
                f"\nInvalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"\nInvalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self):
        print(
            f"\nCurrent plant: {self.name}"
            f"({self.__height}cm, {self.__age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Secureplant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    plant.get_info()
