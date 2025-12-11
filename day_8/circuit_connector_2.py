import math

def process_input(input_file):
    coordinates = []
    with open(input_file, "r", newline='') as f:
        for row in f:
            row = row.strip()
            if row:
                x, y, z = map(int, row.split(","))
                coordinates.append([x, y, z])
    return coordinates


def get_distances(coords):
    distances = []
    ncoords = len(coords)
    for i in range(ncoords):
        for j in range(i + 1, ncoords):
            d = math.dist(coords[i], coords[j])
            distances.append((d, i, j))
    distances.sort(reverse=True)
    return distances


def cfind(n):
    for i, circuit in enumerate(circuits):
        if n in circuit:
            return i
    return None

coordinate_list = process_input("input.csv")
distances = get_distances(coordinate_list)
circuits = [{i} for i in range(len(coordinate_list))]

while distances:
    _, c1, c2 = distances.pop()
    i1, i2 = cfind(c1), cfind(c2)
    if i1 != i2:
        circuits[i1] = circuits[i1] | circuits[i2]
        del circuits[i2]
    if len(circuits) == 1:
        answer = coordinate_list[c1][0] * coordinate_list[c2][0]
        break

circuits.sort(key=lambda c: len(c), reverse=True)
answer
print(answer)
