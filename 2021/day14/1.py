def add_one(key, the_dict):
    if not key:
        return
    if key in the_dict:
        the_dict[key] += 1
    else:
        the_dict[key] = 1


def polymerize(template, rules, occurrences):
    new_template = template[0]
    for i in range(1, len(template)):
        pair = template[i-1] + template[i]
        insertion = rules.get(pair, '')
        add_one(insertion, occurrences)
        new_template += insertion + template[i]
    return new_template


with open('data.in') as f:
    lines = f.read().splitlines()

template = lines[0]
rules = dict()
for line in lines[2:]:
    pair, insertion = line.split(' -> ')
    rules[pair] = insertion

steps = 10
occurrences = dict()
for c in template:
    add_one(c, occurrences)
for i in range(steps):
    template = polymerize(template, rules, occurrences)
print(f'After step {steps} the template length is {len(template)}')
results = sorted(list(occurrences.values()))
print(int(results[len(results)-1]) - int(results[0]))
