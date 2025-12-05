valid_ingredients = []
count = 0

with open("input.csv", "r", newline='') as ingredients:
    for row in ingredients:
        row = row.strip()
        if not row:
            continue

        if "-" in row:
            print("Found Range: " + row)
            start_val, end_val = map(int, row.split("-"))
            valid_ingredients.append((start_val, end_val))
        
        else:
            continue

valid_ingredients.sort(key = lambda x: x[0])
merged = []

for start, end in valid_ingredients:
    if not merged:
        merged.append([start, end])
    else:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

for min_val, max_val in merged:
    count += max_val - min_val + 1

print(count)