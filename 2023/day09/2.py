with open("data.in", "r") as f:
    lines = f.readlines()

result = []
for line in lines:
    sequence = [int(x) for x in line.split(" ")]
    diff_sum = -1
    first = []
    last_value = 0
    while diff_sum != 0:
        first.append(sequence[0])
        pairs = list(zip(sequence, sequence[1:]))
        sequence = [x[1] - x[0] for x in pairs]
        diff_sum = sum(sequence)
    new_result = 0
    for value in reversed(first):
        new_result = value - new_result
    result.append(new_result)
print(sum(result))
