import csv

def find_max_joltage(array):
    max_digit = -1
    for i in array:
        if (i > max_digit):
            max_digit = i

    if(max_digit == -1):
        return None
    
    idx = array.index(max_digit)
    if(idx == (len(array) - 1)):
        return str(max(array[:idx])) + str(max_digit)
    
    else:
        return str(max_digit) + str(max(array[idx + 1:]))
        

banks = []
sum = 0
with open("input.csv", 'r', newline='') as batteries:
    for row in batteries:
        banks.append(row.strip())

int_banks = [[int(d) for d in n] for n in banks]

for bank in int_banks:
    sum += int(find_max_joltage(bank))
    print(find_max_joltage(bank))
print(sum)