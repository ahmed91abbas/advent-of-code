with open("data.in", "r") as f:
    lines = f.read().splitlines()

matrix = [[int(x) for x in [*row]] for row in lines]


def visible_from_upper_edge(x, y):
    value = matrix[x][y]
    for i in reversed(range(x)):
        if value <= matrix[i][y]:
            return False
    return True


def visible_from_lower_edge(x, y):
    value = matrix[x][y]
    for i in range(x + 1, len(matrix)):
        if value <= matrix[i][y]:
            return False
    return True


def visible_from_left_edge(x, y):
    value = matrix[x][y]
    for i in reversed(range(y)):
        if value <= matrix[x][i]:
            return False
    return True


def visible_from_right_edge(x, y):
    value = matrix[x][y]
    for i in range(y + 1, len(matrix[0])):
        if value <= matrix[x][i]:
            return False
    return True


result = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if (
            visible_from_upper_edge(i, j)
            or visible_from_lower_edge(i, j)
            or visible_from_left_edge(i, j)
            or visible_from_right_edge(i, j)
        ):
            result += 1
print(result)
