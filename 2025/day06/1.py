import math

with open("data.in") as f:
    lines = f.read().splitlines()

gragh = []
for line in lines[:-1]:
    gragh.append([int(x) for x in line.split()])
flipped = list(map(list, zip(*gragh)))
operations = lines[len(lines) - 1].split()

answer = 0
for i, op in enumerate(operations):
    if op == "+":
        answer += sum(flipped[i])
    elif op == "*":
        answer += math.prod(flipped[i])

print(answer)
