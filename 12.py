from collections import deque
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file")

args = parser.parse_args()

filepath = args.file
with open(filepath) as f:
	lines = [line.rstrip() for line in f]

total = 0
for line in lines:
	conditions_short, sizes_str = line.split()
	sizes_short = [int(x) for x in sizes_str.split(',')]

	conditions = conditions_short
	sizes = sizes_short.copy()
	for _ in range(4):
		conditions += '?' + conditions_short
		sizes.extend(sizes_short)

	mem = dict()
	def get_possibilities(idx_conditions, idx_sizes):
		if idx_conditions >= len(conditions):
			if idx_sizes == len(sizes): 
		 		return 1
			else:
				return 0
		if (idx_conditions, idx_sizes) in mem.keys():
			return mem[(idx_conditions, idx_sizes)]

		result = None
		if conditions[idx_conditions] == '.':
			result = get_possibilities(idx_conditions+1, idx_sizes)
		elif idx_sizes == len(sizes):
			if conditions[idx_conditions] == '#':
				result = 0
			else:
				result = get_possibilities(idx_conditions+1, idx_sizes)
		else:
			current_size = sizes[idx_sizes]
			# Match
			current_size_matches = True
			end = idx_conditions + current_size
			if end <= len(conditions):
				for i in range(idx_conditions, end):
					if conditions[i] == '.':
						current_size_matches = False
						break
				if current_size_matches and end < len(conditions) and conditions[end] == '#':
					current_size_matches = False
			else:
				current_size_matches = False

			if conditions[idx_conditions] == '#':
				if current_size_matches:
					result = get_possibilities(idx_conditions+current_size+1, idx_sizes+1)
				else:
					result = 0
			else: # conditions[idx_conditions] == '?':
				result = get_possibilities(idx_conditions+1, idx_sizes)
				if current_size_matches:
					result += get_possibilities(idx_conditions+current_size+1, idx_sizes+1)
		
		mem[(idx_conditions, idx_sizes)] = result
		return result

	possible_arrangements = get_possibilities(0,0)
	print(f"{conditions} {sizes}: {possible_arrangements}")

	total += possible_arrangements

print(total)





