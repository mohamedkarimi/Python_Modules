import math


def get_player_pos():
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        parts = user_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            return (x, y, z)
        except ValueError as e:
            bad_value = ""
            for part in parts:
                try:
                    float(part)
                except ValueError:
                    bad_value = part.strip()
                    break
            print("Error on parameter '" + bad_value + "':", e)


print("=== Game Coordinate System ===")

print("Get a first set of coordinates")
pos1 = get_player_pos()

print("Got a first tuple:", pos1)

x1, y1, z1 = pos1
print("It includes: X=" + str(x1) + ", Y=" + str(y1) + ", Z=" + str(z1))

distance_to_center = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
print("Distance to center:", round(distance_to_center, 4))

print("Get a second set of coordinates")
pos2 = get_player_pos()
