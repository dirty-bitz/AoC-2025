import math

def process_input(input_file):
    coordinates = []
    with open(input_file, "r", newline = '') as f:
        for row in f:
            row = row.strip()
        if row:
            x, y, z = map(int, row.split(","))
            coordinates.append([x, y, z])


    return coordinates
def pair_distance(a, b):
    return math.dist(a, b)

def find_closest(coords):
    min_distance = float("inf")
    closest_pair = None
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            distance = pair_distance(coords[i], coords[j])
        if distance < min_distance:
            min_distance = distance
            closest_pair = (coords[i], coords[j])
    return(closest_pair, min_distance)

coordinate_list = process_input("input.csv")
print(coordinate_list)