with open("data.in") as f:
    lines = f.read().splitlines()

horizontal = 0
depth = 0
aim = 0

for line in lines:
    key, value = line.split(" ")
    value = int(value)
    if key == "forward":
        horizontal += value
        depth += aim * value
    elif key == "down":
        aim += value
    elif key == "up":
        aim -= value

result = horizontal * depth
print(result)
