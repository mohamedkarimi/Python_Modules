def check_temperature(temp_str: str) -> int:
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        return (f"Error: '{temp_str}' is not a valid number\n")

    if 0 <= temp <= 40:
        return f"Temperature {temp}°C is perfect for plants!\n"
    elif temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
    else:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)\n")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    for i in tests:
        try:
            print(check_temperature(i))
        except ValueError as e:
            print(e)
    print("All tests completed - program didn't crash!")


test_temperature_input()
