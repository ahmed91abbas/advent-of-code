def is_valid_update(update, rules):
    for i in range(1, len(update)):
        rule = rules.get(update[i], set())
        if not rule.isdisjoint(update[:i]):
            return False
    return True


with open("data.in") as f:
    lines = f.read().splitlines()

rules = {}
updates = []
for line in lines:
    if "|" in line:
        a, b = line.split("|")
        if a in rules:
            rules[a].add(b)
        else:
            rules[a] = {b}
    elif "," in line:
        updates.append(line.split(","))

res = 0
for update in updates:
    if is_valid_update(update, rules):
        res += int(update[len(update) // 2])
print(res)
