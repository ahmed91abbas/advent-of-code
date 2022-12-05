def get_diff(smaller, bigger):
    return [x for x in bigger if x not in smaller]


def get_mapping(patterns):
    mappings = {}
    # find out mapping for a
    mappings["a"] = get_diff(patterns[0], patterns[1])[0]
    # find out mapping for d
    bd = get_diff(patterns[0], patterns[2])
    mappings["d"] = bd[0]
    for i in range(3, 6):
        if bd[0] not in patterns[i]:
            mappings["d"] = bd[1]
            break
    # find out mapping for b
    mappings["b"] = get_diff([mappings["d"]], bd)[0]
    # find out mapping for g
    nine_without_bottom = patterns[2] + mappings["a"]
    for i in range(6, 9):
        diff = get_diff(nine_without_bottom, patterns[i])
        if len(diff) == 1:
            mappings["g"] = diff[0]
    # find out mapping for e
    eight_without_e = patterns[2] + mappings["a"] + mappings["g"]
    mappings["e"] = get_diff(eight_without_e, patterns[9])[0]
    # find out mapping for c
    two_without_c = mappings["a"] + mappings["d"] + mappings["e"] + mappings["g"]
    for i in range(3, 6):
        diff = get_diff(two_without_c, patterns[i])
        if len(diff) == 1:
            mappings["c"] = diff[0]
    # find out mapping for f
    mappings["f"] = get_diff([mappings["c"]], patterns[0])[0]

    return mappings


with open("data.in") as f:
    lines = f.read().splitlines()

digit_mappings = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


result = 0
for line in lines:
    p, o = line.split("|")
    patterns = sorted(p.split(), key=len)
    outputs = o.split()
    mappings = get_mapping(patterns)
    num = ""
    for output in outputs:
        r = []
        for c in output:
            for k, v in mappings.items():
                if c == v:
                    r.append(k)
        key = "".join(sorted(r))
        num += digit_mappings[key]
    result += int(num)

print(result)
