def rotate(matrix):
    rotated = ["".join(row) for row in zip(*matrix[::-1])]
    return rotated


def get_count(matrix):
    res = 0
    for i in range(len(matrix)):
        row = ""
        diagonal_r = ""
        diagonal_l = ""
        for j in range(len(matrix[0])):
            row += matrix[i][j]
            if i + j < len(matrix[0]) and j < len(matrix):
                diagonal_r += matrix[j][i + j]
            if i + j + 1 < len(matrix):
                diagonal_l += matrix[i + j + 1][j]
        res += row.count("XMAS")
        res += row.count("SAMX")
        res += diagonal_r.count("XMAS")
        res += diagonal_r.count("SAMX")
        res += diagonal_l.count("XMAS")
        res += diagonal_l.count("SAMX")
    return res


with open("data.in") as f:
    matrix = f.read().splitlines()

res = get_count(matrix)
res += get_count(rotate(matrix))
print(res)
