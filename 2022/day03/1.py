import string

with open("data.in", "r") as f:
    lines = f.read().splitlines()

letters = string.ascii_lowercase + string.ascii_uppercase
result = 0
for line in lines:
    set1 = set(line[0:len(line)//2])
    set2 = set(line[len(line)//2:])
    intersection = set1.intersection(set2)
    result += letters.index(intersection.pop()) + 1

print(result)
