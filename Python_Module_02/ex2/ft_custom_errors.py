class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def plant(is_wilting):
    if is_wilting:
        raise PlantError("The tomato plant is wilting")


def water(water_amount):
    if water_amount < 10:
        raise WaterError("Not enough water in the tank\n")


print("=== Custom Garden Errors Demo ===\n")
try:
    print("Testing PlantError...")
    plant(True)
except PlantError as e:
    print("Caught PlantError:", e)

try:
    print("\nTesting WaterError...")
    water(5)
except WaterError as e:
    print("Caught WaterError:", e)

print("Testing catching all garden errors...")

try:
    plant(True)
except GardenError as e:
    print("Caught a garden error:", e)

try:
    water(5)
except GardenError as e:
    print("Caught a garden error:", e)

print("All custom error types work correctly!")
