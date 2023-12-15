with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]

assert len(lines) == 1
steps = lines[0].split(",")
result = 0
for step in steps:
    hash = 0
    for c in step:
        hash += ord(c)
        hash *= 17
        hash %= 256
    result += hash

print(result)
