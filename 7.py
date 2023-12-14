with open('./7.txt') as f:
	lines = [line.rstrip().split() for line in f]
hands = [(line[0], int(line[1])) for line in lines]

def type_rank(hand: str):
	card_count = dict()
	for c in hand:
		card_count[c] = card_count.get(c, 0) + 1
	counts = list(card_count.values())
	if 5 in counts:
		return 6
	if 4 in counts:
		return 5
	if 3 in counts and 2 in counts:
		return 4
	if 3 in counts:
		return 3
	if len([count for count in counts if count == 2]) == 2:
		return 2
	if 2 in counts:
		return 1
	return 0

def get_hand_key(hand: str):
	card_val = { 'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10 }
	for c in range(2,10):
		card_val[str(c)] = c
	possible_types = [ type_rank(hand.replace('J', c)) for c in card_val.keys() if c != 'J']
	hand_key = [ max(possible_types) ]
	for c in hand:
		hand_key.append(card_val[c])
	return hand_key

hands.sort(key=lambda hand_and_bid: get_hand_key(hand_and_bid[0]))

for hand in hands:
	print(hand[0] + " " + str(get_hand_key(hand[0])))

score = 0
rank = 1
for hand, bid in hands:
	score += rank * bid
	rank += 1
print(score)