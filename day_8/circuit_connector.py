def process_input(input_file):
    list = []
    with open(input_file, "r", newline = '') as f:
        for row in f:
            list.append(row.rstrip("\n"))

    return list

coordinate_list = process_input("input.csv")
print(coordinate_list)