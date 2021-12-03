with open('data.in') as f:
    rows = f.read().splitlines()

bits = [0] * len(rows[0])
for r in rows:
    for i, c in enumerate(r):
        bits[i] += int(c)

b_gamma = ''.join(['1' if int(b) > len(rows)//2 else '0' for b in bits])
b_epsilon = ''.join(['1' if i == '0' else '0' for i in b_gamma])
result = int(b_gamma, 2) * int(b_epsilon, 2)
print(result)
