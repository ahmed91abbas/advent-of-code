with open("data.in", "r") as f:
    lines = f.read().splitlines()

rock = ["A", "X", 1]
paper = ["B", "Y", 2]
scissors = ["C", "Z", 3]
result = 0
for line in lines:
    first, second = line.split()
    if first in rock and second in rock:
        result += 3 + rock[2]
    elif first in rock and second in paper:
        result += 6 + paper[2]
    elif first in rock and second in scissors:
        result += 0 + scissors[2]
    elif first in paper and second in rock:
        result += 0 + rock[2]
    elif first in paper and second in paper:
        result += 3 + paper[2]
    elif first in paper and second in scissors:
        result += 6 + scissors[2]
    elif first in scissors and second in rock:
        result += 6 + rock[2]
    elif first in scissors and second in paper:
        result += 0 + paper[2]
    elif first in scissors and second in scissors:
        result += 3 + scissors[2]
print(result)
