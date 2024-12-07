with open("data.in") as f:
    matrix = f.read().splitlines()

res = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        right = (i, j + 2)
        left_d = (i, j + 2)
        right_d = (i + 2, j + 2)
        if i + 2 < len(matrix) and j + 2 < len(matrix[0]):
            middle = matrix[i + 1][j + 1]
            left = matrix[i][j]
            right = matrix[i + 2][j]
            left_d = matrix[i][j + 2]
            right_d = matrix[i + 2][j + 2]
            first = left + middle + right_d
            second = right + middle + left_d
            if (first == "MAS" or first == "SAM") and (second == "MAS" or second == "SAM"):
                res += 1
print(res)
