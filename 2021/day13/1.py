def fold(marked, instruction):
    new_marked = set()
    axis, value = instruction.split("=")
    value = int(value)
    for x, y in marked:
        if axis == "y":
            if y > value:
                new_marked.add((x, value * 2 - y))
            elif y < value:
                new_marked.add((x, y))
        if axis == "x":
            if x > value:
                new_marked.add((value * 2 - x, y))
            elif x < value:
                new_marked.add((x, y))
    return new_marked


with open("data.in") as f:
    lines = f.read().splitlines()

marked = set()
instructions = []
for line in lines:
    if "fold" in line:
        instructions.append(line.replace("fold along ", ""))
    elif "," in line:
        x, y = map(int, line.split(","))
        marked.add((x, y))

for instruction in instructions:
    marked = fold(marked, instruction)
    print(len(marked))
    break
