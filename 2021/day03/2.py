with open('data.in') as f:
    rows = f.read().splitlines()

def filter_list(b_list, index, value_for_most_common, value_for_least_common):
    bits = [0] * len(b_list[0])
    for r in b_list:
        for i, c in enumerate(r):
            bits[i] += int(c)
    result = list()
    bit_to_keep = value_for_most_common if bits[index] >= len(b_list) - bits[index] else value_for_least_common
    for i, row in enumerate(b_list):
        if row[index] == bit_to_keep:
            result.append(row)
    return result

def get_rating(rows, value_for_most_common, value_for_least_common):
    b_list = rows.copy()
    index = 0
    while len(b_list) > 1:
        b_list = filter_list(b_list, index, value_for_most_common, value_for_least_common)
        index += 1
    return int(b_list[0], 2)

o2 = get_rating(rows, '1', '0')
co2 = get_rating(rows, '0', '1')

result = o2 * co2
print(result)
