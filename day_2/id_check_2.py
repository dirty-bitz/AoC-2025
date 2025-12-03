import csv

def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)
    
    for i in range(1, length // 2 + 1):
        if length % i != 0:
            continue
        block = s[:i]
        if block * (length // i) == s:
            return True
    return False


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
