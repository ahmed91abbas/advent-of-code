with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def get_combinations(data, groups, data_index, group_index):
    if group_index == len(groups):
        return 1 if "#" not in data[data_index:] else 0

    combinations = 0
    for i in range(data_index, len(data)):
        current = data[i : i + groups[group_index]]
        if (
            len(current) == groups[group_index]
            and "." not in current
            and (len(data) <= i + groups[group_index] or data[i + groups[group_index]] != "#")
        ):
            combinations += get_combinations(data, groups, i + groups[group_index] + 1, group_index + 1)
        if data[i] == "#":
            break

    return combinations


result = 0
for line in lines:
    p1, p2 = line.split(" ")
    data = list(p1)
    groups = [int(x) for x in p2.split(",")]
    result += get_combinations(data, groups, 0, 0)

print(result)
