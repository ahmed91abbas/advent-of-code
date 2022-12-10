with open("data.in", "r") as f:
    lines = f.read().splitlines()

cycles = 0
x = 1
result = 0
signals = [20, 60, 100, 140, 180, 220]
for line in lines:
    if line == "noop":
        cycles += 1
        if cycles in signals:
            print(cycles, x, cycles * x)
            result += cycles * x
    else:
        if (cycles + 1) in signals:
            result += (cycles + 1) * x
            print(cycles + 1, x, (cycles + 1) * x)
        cycles += 2
        if cycles in signals:
            print(cycles, x, cycles * x)
            result += cycles * x
        x = x + int(line.split(" ")[1])

print(result)
