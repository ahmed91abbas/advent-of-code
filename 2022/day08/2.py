with open("data.in", "r") as f:
    lines = f.read().splitlines()

matrix = [[int(x) for x in [*row]] for row in lines]


def visible_upper_count(x, y):
    value = matrix[x][y]
    trees = 0
    for i in reversed(range(x)):
        if value <= matrix[i][y]:
            return trees + 1
        else:
            trees += 1
    return trees


def visible_lower_count(x, y):
    value = matrix[x][y]
    trees = 0
    for i in range(x + 1, len(matrix)):
        if value <= matrix[i][y]:
            return trees + 1
        else:
            trees += 1
    return trees


def visible_from_left_count(x, y):
    value = matrix[x][y]
    trees = 0
    for i in reversed(range(y)):
        if value <= matrix[x][i]:
            return trees + 1
        else:
            trees += 1
    return trees


def visible_from_right_count(x, y):
    value = matrix[x][y]
    trees = 0
    for i in range(y + 1, len(matrix[0])):
        if value <= matrix[x][i]:
            return trees + 1
        else:
            trees += 1
    return trees


max = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        current = (
            visible_upper_count(i, j)
            * visible_lower_count(i, j)
            * visible_from_left_count(i, j)
            * visible_from_right_count(i, j)
        )
        if current > max:
            max = current
print(max)
