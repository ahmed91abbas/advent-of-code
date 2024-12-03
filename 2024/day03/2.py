import re

pattern = re.compile("mul\\((\\d+),(\\d+)\\)")


def get_result(line):
    matches = re.findall(pattern, line)
    res = 0
    for match in matches:
        res += int(match[0]) * int(match[1])
    return res


with open("data.in") as f:
    data = f.read().strip()

parts = data.split("don't()")
res = get_result(parts[0])
for i in range(1, len(parts)):
    dos = parts[i].split("do()")
    if len(dos) > 1:
        for i in range(1, len(dos)):
            res += get_result(dos[i])

print(res)
