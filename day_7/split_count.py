def count_splits_unique(grid):
    height = len(grid)
    width = len(grid[0])
    
    current_beams = set()
    
    start_x = grid[0].index("S")
    current_beams.add(start_x)
    
    split_count = 0
    
    for y in range(1, height):
        next_beams = set()
        
        for x in current_beams:
            cell = grid[y][x]
            if cell == ".":
                next_beams.add(x)
            elif cell == "^":
                split_count += 1
                if x > 0:
                    next_beams.add(x-1)
                if x < width-1:
                    next_beams.add(x+1)
            else:
                # shouldn't happen
                next_beams.add(x)
                
        current_beams = next_beams
    
    return split_count

grid = [list(line.rstrip("\n")) for line in open("input.csv")]
print(count_splits_unique(grid))

