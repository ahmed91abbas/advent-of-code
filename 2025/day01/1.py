with open("data.in") as f:
    lines = f.read().splitlines()

current = 50
answer = 0
for line in lines:
    direction = line[0]
    value = int(line[1:])
    value = value if direction == "R" else -value
    current = (current + value) % 100
    if current == 0:
        answer += 1

print(answer)
