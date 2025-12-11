def process_input(input):
    pts = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(","))
                pts.append((x, y))
    return pts

def largest_rectangle(points):
    largest = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > largest:
                largest = area
    return largest

tiles = process_input("input.csv")
print(largest_rectangle(tiles))