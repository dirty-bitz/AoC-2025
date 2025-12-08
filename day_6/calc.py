import csv
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

columns = []
results = []

with open("input.csv", 'r') as input:
    hw = list(csv.reader(input, delimiter=' '))
    
    cleaned_rows = []
    for row in hw:
        cleaned_row = []
        for cell in row:
            if cell != '':
                cleaned_row.append(cell)
        cleaned_rows.append(cleaned_row)
    
    hw = cleaned_rows
    op_row = hw[-1]
    data_rows = hw[:-1]
    columns = list(zip(*data_rows))

columns = [list(map(int, col)) for col in columns]

for column, op_symbol in zip(columns, op_row):
    op_func = ops[op_symbol]
    result = column[0]
    for value in column[1:]:
        result = op_func(result, value)

    results.append(result)
print(results)
print(sum(results))