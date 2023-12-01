with open("data.in") as f:
    lines = f.read().splitlines()

sum = 0
for line in lines:
    digits = [c for c in line if c.isdigit()]
    if digits:
        sum += int(digits[0] + digits[-1])
print(sum)
