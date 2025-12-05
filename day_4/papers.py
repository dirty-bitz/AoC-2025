import csv

def count_adjacent(array):
    directions = {(-1, -1), (0, -1), (1, -1)
                  (-1, 0),           (1, 0),
                  (-1, 1),  (0, 1),  (1, 1)}

papers = []
papers_arrays = []
with open("input.csv", 'r', newline='') as input:
    for row in input:
        papers.append(row.strip())
for roll in papers:
    papers_arrays.append([[char] for char in roll])
print(papers_arrays)