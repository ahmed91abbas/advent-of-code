import math


def split_at_indices(s, indices):
    result = []
    prev = 0
    for idx in indices:
        result.append(s[prev:idx])
        prev = idx + 1
    result.append(s[prev:])
    return result


with open("data.in") as f:
    lines = f.read().splitlines()

split_indices = []
for i, c in enumerate(lines[len(lines) - 1]):
    if (c == "+" or c == "*") and i != 0:
        split_indices.append(i - 1)

gragh = []
for line in lines[:-1]:
    gragh.append([x for x in split_at_indices(line, split_indices)])
flipped = list(map(list, zip(*gragh)))

operations = lines[len(lines) - 1].split()
answer = 0
for i, op in enumerate(operations):
    current = list(map(list, zip(*flipped[i])))
    current = [int(num) for num in ["".join(x) for x in current]]
    if op == "+":
        answer += sum(current)
    elif op == "*":
        answer += math.prod(current)

print(answer)
