def water_plants(plant_list):
    print("Opening watering system")
    i = 0
    try:
        while i < len(plant_list):
            if plant_list[i] is None:
                raise Exception(" Cannot water None - invalid plant!")
            print(f"Watering {plant_list[i]}")
            i += 1
    except Exception as e:
        print("Error:", e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    bad_plants = ["tomato", None, "carrots"]
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")


test_watering_system()
