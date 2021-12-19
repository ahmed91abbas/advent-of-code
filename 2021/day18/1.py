import re
import math


def explode(pairs):
    depth = 0
    current = ''
    i = -1
    while (depth < 5 or not current.isdigit()) and i < len(pairs)-1:
        i += 1
        current = pairs[i]
        if current == '[':
            depth += 1
        elif current == ']':
            depth -= 1
    if i == len(pairs)-1:
        return pairs
    start = i - 1
    end = start + pairs[start:].index(']')
    n1, n2 = map(int, pairs[start+1:end].split(','))
    left_start = None
    for match in re.finditer('[0-9]+', pairs[:start-1]):
        left_start, left_end = match.span()
    left_part = pairs[:start]
    if left_start:
        left_part = f'{pairs[:left_start]}{int(pairs[left_start:left_end])+n1}{pairs[left_end:start]}'
    right_part = pairs[end+1:]
    right_values = [x for x in pairs[end+1:].replace('[', '').replace(']', '').split(',') if x]
    if right_values:
        right_start = right_part.index(right_values[0]) + end + 1
        right_end = right_start + len(right_values[0])
        right_part = f'{pairs[end+1:right_start]}{int(pairs[right_start:right_end])+n2}{pairs[right_end:]}'

    return left_part + '0' + right_part


def split(pairs):
    x = re.search('[0-9]{2,}', pairs)
    if x:
        start = x.start()
        end = x.end()
        nbr = int(pairs[start:end])
        return f'{pairs[:start]}[{nbr//2},{math.ceil(nbr/2)}]{pairs[end:]}'
    return pairs


def add(pairs1, pairs2):
    return f'[{pairs1},{pairs2}]'


def get_magnitude(pairs):
    while True:
        x = re.search('\[[0-9]+,[0-9]+]', pairs)
        if not x:
            return pairs
        s, e = x.span()
        l, r = pairs[s+1:e-1].split(',')
        magnitude = 3*int(l) + 2*int(r)
        pairs = f'{pairs[:s]}{magnitude}{pairs[e:]}'


with open('data.in') as f:
    lines = f.read().splitlines()

current = lines[0]
for line in lines[1:]:
    current = add(current, line)
    prev = None
    while current != prev:
        prev = current
        current = explode(current)
    prev = None
    while current != prev:
        prev = current
        current = split(current)
        current = explode(current)
print(current)
print(get_magnitude(current))
