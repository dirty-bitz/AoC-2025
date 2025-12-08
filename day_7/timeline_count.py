def count_quantum_timelines(grid):
    height = len(grid)
    width = len(grid[0])

    start_x = grid[0].index("S")
    
    prev_row = [0] * width
    prev_row[start_x] = 1
    
    for y in range(1, height):
        curr_row = [0] * width
        for x in range(width):
            count = prev_row[x]
            if count == 0:
                continue
            cell = grid[y][x]
            if cell == ".":
                curr_row[x] += count
            elif cell == "^":
                if x > 0:
                    curr_row[x-1] += count
                if x < width-1:
                    curr_row[x+1] += count
            else:
                curr_row[x] += count
        prev_row = curr_row
    
    return sum(prev_row)

grid = [list(line.rstrip("\n")) for line in open("input.csv")]

print("Total quantum timelines:", count_quantum_timelines(grid))
