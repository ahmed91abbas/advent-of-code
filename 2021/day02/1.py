with open("data.in") as f:
    lines = f.read().splitlines()

directions = {"forward": 0, "down": 0, "up": 0}
for line in lines:
    key, value = line.split(" ")
    directions[key] += int(value)

result = directions["forward"] * (directions["down"] - directions["up"])
print(result)
