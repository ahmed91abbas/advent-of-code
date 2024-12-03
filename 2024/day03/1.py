import re

with open("data.in") as f:
    data = f.read().strip()

pattern = re.compile("mul\\((\\d+),(\\d+)\\)")
matches = re.findall(pattern, data)
res = 0
for match in matches:
    res += int(match[0]) * int(match[1])

print(res)
