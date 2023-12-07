from collections import defaultdict

with open("data.in", "r") as f:
    lines = f.readlines()

order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

hands = {}
for line in lines:
    hand, bid = line.strip().split(" ")
    hands[hand] = bid


def card_strength_by_type(ori_card):
    card = replace_joker(ori_card)
    # Five of a kind
    if len(set(card)) == 1:
        return 7
    # Four of a kind
    for c in card:
        if card.count(c) == 4:
            return 6
    # Full house
    unique_values = set(card)
    if len(unique_values) == 2 and (
        card.count(list(unique_values)[0]) == 3 or card.count(list(unique_values)[1]) == 3
    ):
        return 5
    # Three of a kind
    for c in card:
        if card.count(c) == 3:
            return 4
    # Two pair
    unique_pairs = [c for c in unique_values if card.count(c) == 2]
    if len(unique_pairs) == 2:
        return 3
    # One pair
    for c in card:
        if card.count(c) == 2:
            return 2
    # High card
    return 1


def replace_joker(hand):
    if "J" not in hand:
        return hand
    if hand == "JJJJJ":
        return "AAAAA"
    cards = sorted(hand.replace("J", ""), key=lambda x: order.index(x), reverse=True)
    most_common_char = max(set(cards), key=cards.count)
    return hand.replace("J", most_common_char)


def get_hand_value(hand):
    value = 0
    for c in hand:
        value = value * 13 + order.index(c)
    return value


hand_per_type = {}
for hand in hands:
    hand_per_type[hand] = card_strength_by_type(hand)

sorted_hands = sorted(hand_per_type.items(), key=lambda x: x[1])
grouped_hands = defaultdict(list)
for k, v in sorted_hands:
    grouped_hands[v].append(k)

current_rank = 1
result = 0
for group in grouped_hands.values():
    for hand in sorted(group, key=get_hand_value):
        result += current_rank * int(hands[hand])
        current_rank += 1

print(result)
