from collections import defaultdict, Counter


def polymerize(pairs, rules):
    new_pairs = defaultdict(int)
    for (c1, c2), v in pairs.items():
        pair1 = c1 + rules[c1 + c2]
        pair2 = rules[c1 + c2] + c2
        new_pairs[pair1] += v
        new_pairs[pair2] += v
    return new_pairs


with open("data.in") as f:
    lines = f.read().splitlines()

template = lines[0]
rules = dict()
for line in lines[2:]:
    pair, insertion = line.split(" -> ")
    rules[pair] = insertion

pairs = Counter([c1 + c2 for c1, c2 in zip(template, template[1:])])

steps = 40
for _ in range(steps):
    pairs = polymerize(pairs, rules)

chars_count = defaultdict(int)
for (c1, c2), v in pairs.items():
    chars_count[c1] += v
chars_count[c2] += 1

results = sorted(list(chars_count.values()))
print(int(results[len(results) - 1]) - int(results[0]))
