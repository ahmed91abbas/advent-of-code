with open("data.in", "r") as f:
    lines = f.read()
values = lines.split("\n")
current = 0
sums = []
for x in values:
    if x:
        current += int(x)
    else:
        sums.append(current)
        current = 0

print(max(sums))
