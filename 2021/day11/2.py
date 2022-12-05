def get_neighbors(a, b, matrix):
    d = {(i, c): matrix[i][c] for i in range(len(matrix)) for c in range(len(matrix[0]))}
    return [
        i
        for i in [
            (a + 1, b + 1),
            (a - 1, b - 1),
            (a, b + 1),
            (a + 1, b),
            (a - 1, b + 1),
            (a - 1, b),
            (a, b - 1),
            (a + 1, b - 1),
        ]
        if d.get(i)
    ]


def flash_octopus(i, j, matrix, flashed):
    if (i, j) in flashed:
        return
    flashed.add((i, j))
    neighbors = get_neighbors(i, j, matrix)
    for i, j in neighbors:
        matrix[i][j] += 1
    for i, j in neighbors:
        if matrix[i][j] > 9:
            flash_octopus(i, j, matrix, flashed)


with open("data.in") as f:
    lines = f.read().splitlines()

matrix = [[int(oct) for oct in line] for line in lines]

step = 0
while True:
    step += 1
    matrix = [[oct + 1 for oct in row] for row in matrix]
    flashed = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 9:
                flash_octopus(i, j, matrix, flashed)
    for i, j in flashed:
        matrix[i][j] = 0
    if len(flashed) == len(matrix) * len(matrix):
        print(step)
        break
