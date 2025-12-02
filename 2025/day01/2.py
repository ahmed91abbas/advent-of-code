with open("data.in") as f:
    lines = f.read().splitlines()

current = 50
answer = 0
for line in lines:
    direction = line[0]
    value = int(line[1:])
    signed_value = value if direction == "R" else -value
    if value >= 100:
        answer += value // 100
        value = value % 100
    if direction == "L" and current - value <= 0 and current != 0:
        answer += 1
    if direction == "R" and current + value >= 100 and current != 0:
        answer += 1
    current = (current + signed_value) % 100

print(answer)
