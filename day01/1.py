with open('data.in') as f:
    lines = f.read().splitlines()
    result = 0
    prev = int(lines[0])
    for i in range(1, len(lines)):
        current = int(lines[i])
        if current > prev:
            result += 1
        prev = current
print(result)
