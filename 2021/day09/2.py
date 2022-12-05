def get_adjacent_indices(i, j, matrix):
    indices = []
    # up
    if i > 0:
        indices.append((i - 1, j))
    # down
    if i < len(matrix) - 1:
        indices.append((i + 1, j))
    # left
    if j > 0:
        indices.append((i, j - 1))
    # right
    if j < len(matrix[i]) - 1:
        indices.append((i, j + 1))
    return [x for x in indices if matrix[x[0]][x[1]] != 9]


def get_basin_size(i, j, matrix, visited):
    queue = set()
    queue.update([(i, j)] if matrix[i][j] != 9 else [])
    size = 0
    while queue:
        elem = queue.pop()
        visited.add(elem)
        queue.update([x for x in get_adjacent_indices(elem[0], elem[1], matrix) if x not in visited])
        size += 1
    return size


with open("data.in") as f:
    lines = f.read().splitlines()

matrix = []
for line in lines:
    matrix.append([int(x) for x in line])

basins = []
visited = set()
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if (i, j) in visited:
            continue
        basin = get_basin_size(i, j, matrix, visited)
        basins.append(basin)

sorted = sorted(basins, reverse=True)
print(sorted[0] * sorted[1] * sorted[2])
