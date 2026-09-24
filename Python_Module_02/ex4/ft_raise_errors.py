def check_plant_health(plant_name, water_level, sunlight_hours) -> str:
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!\n")
    if water_level >= 10 or water_level <= 1:
        raise ValueError(
            f"Error: Water level {water_level} is too high (max 10)\n")
    if sunlight_hours >= 12 or sunlight_hours <= 2:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)\n")
    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 6))
    except Exception as e:
        print(e)

    try:
        print("Testing empty plant name...")
        print(check_plant_health("", 5, 6))
    except Exception as e:
        print(e)

    try:
        print("Testing bad water level...")
        print(check_plant_health("let", 15, 6))
    except Exception as e:
        print(e)

    try:
        print("Testing bad sunlight hours...")
        print(check_plant_health("leee", 5, 16))
    except Exception as e:
        print(e)

    finally:
        print("All error raising tests completed!")


test_plant_checks()
