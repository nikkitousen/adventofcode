from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file")

args = parser.parse_args()

filepath = args.file
with open(filepath) as f:
	lines = [line.rstrip() for line in f]

def print_pattern(pattern):
	for line in pattern:
		print(line)

patterns = []
pattern = []
for line in lines:
	if line == '':
		patterns.append(pattern.copy())
		pattern = []
	else:
		pattern.append(line)

if len(pattern) > 0:
	patterns.append(pattern.copy())

# for pattern in patterns:
# 	print_pattern(pattern)
# 	print()

total = 0

for pattern in patterns:
	n = len(pattern)
	m = len(pattern[0])
	horizontal_line = None
	vertical_line = None
	for i in range(1, n):
		# Check if line is between rows i-1 and i
		end = 2*i-1
		reflection_diffs = 0
		for k in range(i):
			rk = end-k
			if rk >= n:
				continue
			for j in range(m):
				if pattern[k][j] != pattern[rk][j]:
					reflection_diffs += 1
			if reflection_diffs > 1:
				break
		if reflection_diffs == 1:
			horizontal_line = i
			break
	for j in range(1, m):
		# Check if line is between columns j-1 and j
		end = 2*j-1
		reflection_diffs = 0
		for k in range(j):
			rk = end-k
			if rk >= m:
				continue
			for i in range(n):
				if pattern[i][k] != pattern[i][rk]:
					reflection_diffs += 1
			if reflection_diffs > 1:
				break
		if reflection_diffs == 1:
			vertical_line = j
			break

	if horizontal_line != None:
		total += 100 * horizontal_line
	if vertical_line != None:
		total += vertical_line

	print(horizontal_line)
	print(vertical_line)
	print("----")

print(total)



	




