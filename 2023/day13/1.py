with open("data.in", "r") as f:
    lines = f.read()


def find_reflection_index(pattern):
    for i in range(1, len(pattern)):
        length = min(i, len(pattern) - i)
        p1 = pattern[i - length : i]
        p2 = pattern[i : i + length][::-1]
        if p1 == p2:
            return i
    return 0


patterns = lines.split("\n\n")
result = 0
for pattern in patterns:
    pattern = [line.strip() for line in pattern.strip().split("\n")]
    transposed = ["".join(elements) for elements in list(zip(*pattern))]
    row_index = find_reflection_index(pattern)
    col_index = find_reflection_index(transposed)
    result += col_index if col_index > row_index else row_index * 100

print(result)
