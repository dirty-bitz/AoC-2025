import csv

def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False

    half = length // 2
    return s[:half] == s[half:]


id_sum = 0

with open('input.csv', 'r', newline='') as input:
    reader = csv.reader(input)
    for row in reader:
        for field in row:
            field = field.strip()
            if "-" in field:
                start, end = map(int, field.split("-"))
                for n in range(start, end + 1):
                    if is_invalid_id(n):
                        id_sum += n

print(id_sum)
