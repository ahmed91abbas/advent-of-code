import re

with open("data.in") as f:
    lines = f.read().splitlines()

color_threshold = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
pattern = re.compile(r"Game (\d+):(.*)")
sets_pattern = re.compile(r"(\d+) (\w+)")
valid_ids = []
for line in lines:
    match = pattern.match(line)
    game_id = int(match.group(1))
    game = match.group(2)
    sets = game.split(";")
    is_valid = True
    for game_set in sets:
        match = sets_pattern.findall(game_set)
        for count, color in match:
            if int(count) > color_threshold[color]:
                is_valid = False
                break
    if is_valid:
        valid_ids.append(game_id)

print(sum(valid_ids))
