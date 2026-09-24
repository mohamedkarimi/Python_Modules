import sys

print("=== Inventory System Analysis ===")

inventory = {}
i = 1

while i < len(sys.argv):
    arg = sys.argv[i]

    if arg.count(":") != 1:
        print("Error - invalid parameter '" + arg + "'")
        i += 1
        continue

    parts = arg.split(":")
    item_name = parts[0]
    quantity_str = parts[1]

    if item_name in inventory:
        print("Redundant item '" + item_name + "' - discarding")
        i += 1
        continue

    try:
        quantity = int(quantity_str)
    except ValueError as e:
        print("Quantity error for '" + item_name + "':", e)
        i += 1
        continue

    inventory.update({item_name: quantity})
    i += 1

print("Got inventory:", inventory)

item_list = list(inventory.keys())
print("Item list:", item_list)

total_quantity = sum(inventory.values())
print("Total quantity of the", len(inventory), "items:", total_quantity)

for item in inventory.keys():
    percentage = round((inventory[item] / total_quantity) * 100, 1)
    print("Item", item, "represents", str(percentage) + "%")

most_item = item_list[0]
least_item = item_list[0]

for item in item_list:
    if inventory[item] > inventory[most_item]:
        most_item = item
    if inventory[item] < inventory[least_item]:
        least_item = item

print("Item most abundant:", most_item, "with quantity", inventory[most_item])
print("Item least abundant:", least_item,
      "with quantity", inventory[least_item])

inventory.update({"magic_item": 1})
print("Updated inventory:", inventory)
