import string

with open("data.in", "r") as f:
    lines = f.read().splitlines()

letters = string.ascii_lowercase + string.ascii_uppercase
result = 0
for i in range(0, len(lines), 3):
    set1 = set(lines[i])
    set2 = set(lines[i + 1])
    set3 = set(lines[i + 2])
    intersection = set1.intersection(set2, set3)
    result += letters.index(intersection.pop()) + 1

print(result)
