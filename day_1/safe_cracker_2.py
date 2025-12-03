import csv

position = 50
zero_count = 0

with open('input.csv', 'r', newline='') as combination:
    reader = csv.reader(combination)
    for row in reader:
        if not row:
            continue
        entry = row[0].strip()
        weight = int(entry[1:])

        if entry[0].upper() == 'R':
            for _ in range(weight):
                position = (position + 1) % 100
                if position == 0:
                    zero_count += 1

        else:
            for _ in range(weight):
                position = (position - 1) % 100
                if position == 0:
                    zero_count += 1

print(zero_count)
