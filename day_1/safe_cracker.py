import csv

position = 50
zero_count = 0

with open('input.csv', 'r', newline='') as combination:
    reader = csv.reader(combination)
    for row in reader:
        entry = row[0].strip()
        weight = int(entry[1:])

        if entry[0] == 'R':
            position = (position + weight) % 100
        else:
            position = (position - weight) % 100
        if position == 0:
            zero_count += 1

print(zero_count)
