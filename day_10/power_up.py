import re
import itertools
import numpy as np


def process_input(path):
    machines = []

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            square = re.search(r"\[(.*?)\]", line).group(1)

            paren_groups = re.findall(r"\((.*?)\)", line)
            paren_lists = [
                [int(x) for x in group.split(",") if x.strip()]
                for group in paren_groups
            ]

            curly = re.search(r"\{(.*?)\}", line).group(1)
            curly_list = [int(x) for x in curly.split(",") if x.strip()]

            machines.append([square] + paren_lists + [curly_list])

    return machines


# Solve Ax = b over GF(2), find minimum-weight solution
def solve_min_presses(pattern, buttons):
    n = len(pattern)
    m = len(buttons)

    # Convert target pattern to vector b
    b = np.array([1 if c == '#' else 0 for c in pattern], dtype=np.uint8)

    # Build matrix A
    A = np.zeros((n, m), dtype=np.uint8)
    for j, btn in enumerate(buttons):
        for idx in btn:
            A[idx, j] = 1

    # Row reduce A into RREF over GF(2)
    A2 = A.copy()
    b2 = b.copy()
    pivot_cols = []
    row = 0
    for col in range(m):
        # Find pivot
        pivot = None
        for r in range(row, n):
            if A2[r, col] == 1:
                pivot = r
                break
        if pivot is None:
            continue
        
        # Swap
        A2[[row, pivot]] = A2[[pivot, row]]
        b2[row], b2[pivot] = b2[pivot], b2[row]

        # Eliminate
        for r in range(n):
            if r != row and A2[r, col] == 1:
                A2[r] ^= A2[row]
                b2[r] ^= b2[row]

        pivot_cols.append(col)
        row += 1
        if row == n:
            break

    # Check for inconsistency
    for r in range(n):
        if not A2[r].any() and b2[r] == 1:
            return float('inf')  # No solution

    # Identify free variables
    pivot_set = set(pivot_cols)
    free_vars = [j for j in range(m) if j not in pivot_set]

    x0 = np.zeros(m, dtype=np.uint8)
    row = 0
    for col in pivot_cols:
        s = b2[row]
        for j in range(col+1, m):
            if A2[row, j] == 1:
                s ^= x0[j]
        x0[col] = s
        row += 1

    # If no free variables, unique solution
    if not free_vars:
        return int(x0.sum())

    # Try all combinations of free variables
    best = float('inf')
    for mask in itertools.product([0,1], repeat=len(free_vars)):
        x = x0.copy()
        for val, var in zip(mask, free_vars):
            x[var] = val

        # Recompute pivot variables given free choices
        xr = x.copy()
        row = 0
        for col in pivot_cols:
            s = b2[row]
            for j in range(col+1, m):
                if A2[row, j] == 1:
                    s ^= xr[j]
            xr[col] = s
            row += 1

        best = min(best, int(xr.sum()))

    return best


def compute_total_presses(path):
    machines = process_input(path)
    total = 0

    for machine in machines:
        pattern = machine[0]
        buttons = machine[1:-1]  # ignore curly braces entirely
        presses = solve_min_presses(pattern, buttons)
        total += presses

    return total

print(compute_total_presses("input.csv"))