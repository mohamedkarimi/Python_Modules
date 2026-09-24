def garden_operations(error_type: str):
    if error_type == "value":
        print("Testing ValueError...")
        int("abc")

    elif error_type == "zero":
        print("Testing ZeroDivisionError...")
        div = 5 / 0
        print(div)

    elif error_type == "file":
        print("Testing FileNotFoundError...")
        file = open("missing.txt")
        file.close()

    elif error_type == "key":
        print("Testing KeyError...")
        plants = {
            "rose": 5
        }
        print(plants["missing_plant"])


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")

    print("Testing multiple errors together...")
    try:
        int("abc")
        x = 5 / 0
        print(x)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


test_error_types()
