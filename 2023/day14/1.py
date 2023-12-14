with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def move_rocks(line):
    indices = [x for x in range(len(line)) if line[x] == "O"]
    new_line = line
    for index in indices:
        next_stop = new_line[index:].find("#")
        if next_stop == -1:
            next_stop = len(new_line[index:])
        chunk = new_line[index : index + next_stop]
        last_dot = chunk.rfind(".")
        if last_dot != -1:
            new_line = new_line[:index] + "." + new_line[index + 1 :]
            new_line = new_line[: index + last_dot] + "O" + new_line[index + last_dot + 1 :]
    return new_line


transposed = ["".join(reversed(elements)) for elements in list(zip(*lines))]
result = 0
for line in transposed:
    new_line = move_rocks(line)
    indices_of_O = [index + 1 for index, char in enumerate(new_line) if char == "O"]
    result += sum(indices_of_O)

print(result)
