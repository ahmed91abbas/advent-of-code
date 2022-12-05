with open("data.in") as f:
    lines = f.read().splitlines()

triplets = [list(map(int, lines[i : i + 3])) for i in range(len(lines) - 2)]
result = 0
prev = sum(triplets[0])
for i in range(1, len(triplets)):
    current = sum(triplets[i])
    if current > prev:
        result += 1
    prev = current
print(result)
