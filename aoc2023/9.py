def get_sequences(sequence):
	result = [sequence]
	current_sequence = sequence
	while True:
		all_zeroes = True
		new_sequence = []
		for i in range(1, len(current_sequence)):
			num = current_sequence[i] - current_sequence[i-1]
			new_sequence.append(num)
			if num != 0:
				all_zeroes = False
		result.append(new_sequence)
		current_sequence = new_sequence
		if all_zeroes:
			break
	return result

def get_next_value(sequences):
	next_val = 0
	sequences_reversed = list(reversed(sequences))
	for i in range(1, len(sequences)):
		next_val = next_val + sequences_reversed[i][-1]
	return next_val

def get_previous_value(sequences):
	prev_val = 0
	sequences_reversed = list(reversed(sequences))
	for i in range(1, len(sequences)):
		prev_val = sequences_reversed[i][0] - prev_val
	return prev_val


with open('./input/9.txt') as f:
	lines = [line.rstrip() for line in f]

total = 0
for line in lines:
	sequence = [int(num) for num in line.split()]
	sequences = get_sequences(sequence)
	next_value = get_next_value(sequences)
	previous_value = get_previous_value(sequences)
	total += previous_value
	print(previous_value)

print(f"Total: {total}")


