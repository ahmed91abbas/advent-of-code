import re
import string

with open("data.in", "r") as f:
    lines = f.read().splitlines()

stack_nbr_index = lines.index("") - 1
stack_count = int(lines[stack_nbr_index].split()[-1])
stacks = [[] for i in range(stack_count)]
for i in reversed(range(stack_nbr_index)):
    for index, c in enumerate(lines[i]):
        if c in string.ascii_uppercase:
            stacks[index // 4].append(c)

for line in lines[stack_nbr_index + 2 :]:
    pattern = re.compile("move ([0-9]+) from ([0-9]+) to ([0-9]+)")
    count, from_q, to_q = map(int, re.match(pattern, line).groups())
    for i in range(count):
        crate = stacks[from_q - 1].pop()
        stacks[to_q - 1].append(crate)

for stack in stacks:
    print(stack[-1], end="")
print()
