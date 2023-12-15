from collections import defaultdict

with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def get_hash(sequence):
    hash = 0
    for c in sequence:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash


assert len(lines) == 1
steps = lines[0].split(",")
boxes = defaultdict(list)
values = {}
for step in steps:
    if step[-1] == "-":
        label = step[:-1]
        key = get_hash(label)
        if label in boxes[key]:
            boxes[key].remove(label)
    else:
        label, value = step.split("=")
        key = get_hash(label)
        if label not in boxes[key]:
            boxes[key].append(label)
        values[label] = int(value)

results = []
for key, box in boxes.items():
    for i, lens in enumerate(box):
        result = 1
        result *= 1 + key
        result *= box.index(lens) + 1
        result *= values[lens]
        results.append(result)

print(sum(results))
