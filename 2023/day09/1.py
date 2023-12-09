with open("data.in", "r") as f:
    lines = f.readlines()

result = []
for line in lines:
    sequence = [int(x) for x in line.split(" ")]
    diff_sum = -1
    last = []
    last_value = 0
    while diff_sum != 0:
        last.append(sequence[-1])
        pairs = list(zip(sequence, sequence[1:]))
        sequence = [x[1] - x[0] for x in pairs]
        diff_sum = sum(sequence)
    result.append(sum(last))
print(sum(result))
