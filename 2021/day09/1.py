def get_adjacent_locations(i, j, matrix):
    locations = []
    # up
    if i > 0:
        locations.append(matrix[i-1][j])
    # down
    if i < len(matrix) - 1:
        locations.append(matrix[i+1][j])
    # left
    if j > 0:
        locations.append(matrix[i][j-1])
    # right
    if j < len(matrix[i]) - 1:
        locations.append(matrix[i][j+1])
    return locations


with open('data.in') as f:
    lines = f.read().splitlines()

matrix = []
for line in lines:
    matrix.append([int(x) for x in line])

low_points = []
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        adjacent = get_adjacent_locations(i, j, matrix)
        if all([col < x for x in adjacent]):
            low_points.append(col)

print(low_points)
result = sum([x+1 for x in low_points])
print(result)
