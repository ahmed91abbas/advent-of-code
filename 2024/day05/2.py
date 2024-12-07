from copy import deepcopy


def fix_update(update, rules):
    bad_index = 0
    valid = False
    while not valid:
        for i in range(1, len(update)):
            rule = rules.get(update[i], set())
            if not rule.isdisjoint(update[:i]):
                bad_index = i
                valid = False
                break
            valid = True
        if not valid:
            update[bad_index - 1], update[bad_index] = update[bad_index], update[bad_index - 1]
    return update


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
    fixed = fix_update(deepcopy(update), rules)
    if fixed != update:
        res += int(fixed[len(fixed) // 2])
print(res)
