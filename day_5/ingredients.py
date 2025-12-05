valid_ingredients = []
inventory = []
count = 0

with open("input.csv", "r", newline='') as ingredients:
    for row in ingredients:
        row = row.strip()
        if not row:
            continue

        if "-" in row:
            print("Found Range: " + row)
            min, max = map(int, row.split("-"))
            valid_ingredients.append((min, max))
        
        else:
            inventory.append(int(row))

for i in inventory:
    if any(start <= i <= end for start, end in valid_ingredients):
        count += 1

print(count)
