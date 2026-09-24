class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def add_plants(self, name):

        if name == "":
            raise PlantError("Plant name cannot be empty!")
        else:
            print(f"Added {name} successfully")

    def water_plants(self, name):
        if name == "":
            raise WaterError("No plant to water")
        else:
            print(f"Watering {name} - success")

    def check_plant_health(self, name, water_level, sunlight_hours):
        if name == "":
            raise PlantError("Error: Plant name cannot be empty!\n")
        if water_level >= 10 or water_level <= 1:
            raise ValueError(
                f"Error checking {name}: Water level {water_level} is too high"
                f" (max 10)\n"
            )
        if sunlight_hours >= 12 or sunlight_hours <= 2:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)\n")
        print(f"{name}: healthy (water: {water_level}, sun: {sunlight_hours})")

    def check_water_tank(self, level):
        if level < 5:
            raise WaterError("Not enough water in tank")
        print("we have enough water in th tank")


def test_garden_management():
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    garden = GardenManager()
    try:
        garden.add_plants("tomato")
        garden.add_plants("lettuce")
        garden.add_plants("")
    except PlantError as e:
        print("Error adding plant:", e)

    print("\nWatering plants...")
    print("Opening watering system")
    try:
        garden.water_plants("tomato")
        garden.water_plants("lettuce")
        # garden.water_plants("")
    except WaterError as e:
        print("Error watering plants:", e)
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    try:
        garden.check_plant_health("tomatto", 5, 8)
        garden.check_plant_health("lettuce", 15, 8)
    except ValueError as e:
        print(e)

    print("Testing error recovery...")
    try:
        garden.check_water_tank(2)
    except WaterError as e:
        print("Caught GardenError:", e)
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


test_garden_management()
