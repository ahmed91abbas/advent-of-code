import math
import re

with open("data.in") as f:
    lines = f.read().splitlines()

pattern = re.compile(r"Game (\d+):(.*)")
sets_pattern = re.compile(r"(\d+) (\w+)")
valid_ids = []
result = 0
for line in lines:
    match = pattern.match(line)
    game_id = int(match.group(1))
    game = match.group(2)
    sets = game.split(";")
    max_set_colors = {"red": 0, "green": 0, "blue": 0}
    for game_set in sets:
        match = sets_pattern.findall(game_set)
        for count, color in match:
            if int(count) > max_set_colors[color]:
                max_set_colors[color] = int(count)
    result += math.prod(max_set_colors.values())

print(result)
