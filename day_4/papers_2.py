def count_adjacent(grid):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    rows = len(grid)
    accessible = 0

    for r in range(rows):
        for c in range(len(grid[r])):

            if grid[r][c] != "@":
                continue

            adj_count = 0 

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
                    if grid[nr][nc] == "@":
                        adj_count += 1

            if adj_count < 4:
                accessible += 1
                papers_arrays[r][c] = "."

    return accessible


papers = []
papers_arrays = []
result = 0

with open("input.csv", 'r') as input:
    for row in input:
        papers.append(row.strip())

for roll in papers:
    papers_arrays.append(list(roll))

while True:
    removed = count_adjacent(papers_arrays)
    if removed == 0:
        break
    result += removed

print(result)
