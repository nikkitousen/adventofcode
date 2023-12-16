from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file")

args = parser.parse_args()

filepath = args.file
with open(filepath) as f:
	grid = [line.rstrip() for line in f]

n = len(grid)
m = len(grid[0])

print(f"The grid is {n}x{m}")


def calc_tiles(start_i, start_j, start_d):

	energized = dict()
	for i in range(n):
		for j in range(m):
			energized[(i,j)] = set()

	 	
	stack = [(start_i, start_j, start_d)]

	while len(stack) > 0:
		i,j,d = stack.pop()

		if i < 0 or i >= n:
			continue
		if j < 0 or j >= m:
			continue
		if d in energized[(i,j)]:
			continue
		
		energized[(i,j)].add(d)

		# go >
		if (d, grid[i][j]) in [('>', '.'), ('>', '-'), ('^', '/'), ('v', '\\'), ('^', '-'), ('v', '-')]:
			stack.append((i, j+1, '>'))
		
		# go ^		
		if (d, grid[i][j]) in [('^', '.'), ('^', '|'), ('>', '/'), ('<', '\\'), ('>', '|'), ('<', '|')]:
			stack.append((i-1, j, '^'))

		# go <
		if (d, grid[i][j]) in [('<', '.'), ('<', '-'), ('v', '/'), ('^', '\\'), ('^', '-'), ('v', '-')]:
			stack.append((i, j-1, '<'))

		# go v:
		if (d, grid[i][j]) in [('v', '.'), ('v', '|'), ('<', '/'), ('>', '\\'), ('>', '|'), ('<', '|')]:
			stack.append((i+1, j, 'v'))

	total = 0
	for i in range(n):
		for j in range(m):
			if len(energized[(i,j)]) > 0:
				total += 1

	return total


max_tiles = 0
for i in range(n):
	max_tiles = max(max_tiles, calc_tiles(i, 0, '>'))
	max_tiles = max(max_tiles, calc_tiles(i, m-1, '<'))

for j in range(m):
	max_tiles = max(max_tiles, calc_tiles(0, j, 'v'))
	max_tiles = max(max_tiles, calc_tiles(n-1, j, '^'))

print(max_tiles)






