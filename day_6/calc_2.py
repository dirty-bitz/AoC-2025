import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def parse_worksheet(filename):
    with open(filename, 'r') as f:
        rows = [line.rstrip('\n') for line in f]

    char_rows = [list(row) for row in rows]

    columns = list(zip(*char_rows))

    num_digit_rows = len(char_rows) - 1

    def is_separator(col):
        return all(c == ' ' for c in col[:num_digit_rows])

    problems = []
    current_problem = []

    for col in columns:
        if is_separator(col):
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(col)

    if current_problem:
        problems.append(current_problem)

    problems.reverse()
    results = []

    for problem in problems:
        problem = [col for col in problem if not is_separator(col)]
        if not problem:
            continue

        operator_symbol = problem[0][-1].strip()
        if operator_symbol not in ops:
            continue
        op_func = ops[operator_symbol]

        numbers = []
        for col in problem:
            digits = col[:-1]
            num_str = ''.join(d for d in digits if d != ' ')
            if num_str:
                numbers.append(int(num_str))

        if not numbers:
            continue

        # Apply operator
        result = numbers[0]
        for n in numbers[1:]:
            result = op_func(result, n)

        results.append(result)

    return results

results = parse_worksheet("input.csv")
print("Problem results:", results)
print("Grand total:", sum(results))
