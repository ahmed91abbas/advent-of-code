import re
from collections import defaultdict

with open("data.in") as f:
    lines = f.read().splitlines()

card_counts = {}
for line in lines:
    parts = line.split(":")
    match = re.search(r"Card\s+(\d+)", parts[0])
    game_id = int(match.group(1))
    cards = parts[1].split("|")
    winnings_numbers = [int(x) for x in cards[0].strip().split()]
    my_numbers = [int(x) for x in cards[1].strip().split()]
    count = 0
    for number in my_numbers:
        if number in winnings_numbers:
            count += 1
    card_counts[game_id] = count

cards = {}
for card in card_counts:
    cards[card] = [i + 1 for i in range(card, card + card_counts[card])]

copies = defaultdict(int)
for card in cards:
    copies[card] += 1
    for sub_card in cards[card]:
        copies[sub_card] += copies[card]

print(sum(copies.values()))
