with open("data.in") as f:
    lines = f.read().splitlines()

closing_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

opening_syntax = {"(": ")", "[": "]", "{": "}", "<": ">"}


def get_first_illegal_char(line):
    opening = list()
    for c in line:
        if c in opening_syntax:
            opening.append(c)
        else:
            last = opening.pop()
            if c != opening_syntax[last]:
                return c
    return ""


result = 0
for line in lines:
    result += closing_scores.get(get_first_illegal_char(line), 0)

print(result)
