with open('data.in') as f:
    lines = f.read().splitlines()

result = 0
for line in lines:
    p, o = line.split('|')
    patterns = p.split()
    outputs = o.split()
    result += sum([1 for x in outputs if len(x) in [2, 3, 4, 7]])

print(result)
