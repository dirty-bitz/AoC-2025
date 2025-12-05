import csv

def find_max_joltage(array, result=None):
    if result is None:
        result = []
    
    if len(result) == 12:
        return int("".join(str(d) for d in result))
    
    remaining_digits = 12 - len(result)
    end_limit = len(array) - remaining_digits + 1
    window = array[:end_limit]
    max_digit = max(window)

    if(max_digit == -1):
        return None
    
    idx = window.index(max_digit)

    result.append(max_digit)
    return find_max_joltage(array[idx + 1:], result)
        

banks = []
sum = 0
with open("input.csv", 'r', newline='') as batteries:
    for row in batteries:
        banks.append(row.strip())

int_banks = [[int(d) for d in n] for n in banks]

for bank in int_banks:
    joltage = find_max_joltage(bank)
    print(joltage)
    sum += joltage
print(sum)