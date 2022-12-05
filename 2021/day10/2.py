with open("data.in") as f:
    lines = f.read().splitlines()

closing_scores = {")": 1, "]": 2, "}": 3, ">": 4}

opening_syntax = {"(": ")", "[": "]", "{": "}", "<": ">"}


def is_valid(line):
    opening = list()
    for c in line:
        if c in opening_syntax:
            opening.append(c)
        else:
            last = opening.pop()
            if c != opening_syntax[last]:
                return False
    return True


def get_missing_syntax(line):
    missing = ""
    opening = list()
    for c in line:
        if c in opening_syntax:
            opening.append(c)
        else:
            opening.pop()
    while opening:
        last = opening.pop()
        missing += opening_syntax[last]
    return missing


def get_score(line):
    score = 0
    for c in line:
        score = score * 5 + closing_scores[c]
    return score


scores = list()
valid_lines = [line for line in lines if is_valid(line)]
for line in valid_lines:
    missing_syntax = get_missing_syntax(line)
    scores.append(get_score(missing_syntax))

print(sorted(scores)[len(scores) // 2])
