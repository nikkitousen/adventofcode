from sortedcontainers import SortedList
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file")

args = parser.parse_args()

filepath = args.file
with open(filepath) as f:
	grid = [line.rstrip() for line in f]

n = len(grid)
m = len(grid[0])

min_consecutive_steps = 4
max_consecutive_steps = 10

def get_neighbours(i, j, direction, consecutive_steps):
	neighbours = list()
	can_continue_straight = True
	
	if direction == 'X':
		neighbours.append((i, j+1, '>', 1))
		neighbours.append((i+1, j, 'v', 1))
	if direction == '>':
		if i > 0 and consecutive_steps >= min_consecutive_steps:
			neighbours.append((i-1, j, '^', 1))
		if i < n-1 and consecutive_steps >= min_consecutive_steps:
			neighbours.append((i+1, j, 'v', 1))
		if j < m-1 and consecutive_steps < max_consecutive_steps:
			neighbours.append((i, j+1, '>', consecutive_steps+1))
	if direction == 'v':
		if j > 0 and consecutive_steps >= min_consecutive_steps:
			neighbours.append((i, j-1, '<', 1))
		if j < m-1 and consecutive_steps >= min_consecutive_steps:
			neighbours.append((i, j+1, '>', 1))
		if i < n-1 and consecutive_steps < max_consecutive_steps:
			neighbours.append((i+1, j, 'v', consecutive_steps+1))
	if direction == '<':
		if i > 0 and consecutive_steps >= min_consecutive_steps:
			neighbours.append((i-1, j, '^', 1))
		if i < n-1 and consecutive_steps >= min_consecutive_steps:
			neighbours.append((i+1, j, 'v', 1))
		if j > 0 and consecutive_steps < max_consecutive_steps:
			neighbours.append((i, j-1, '<', consecutive_steps+1))
	if direction == '^':
		if j > 0 and consecutive_steps >= min_consecutive_steps:
			neighbours.append((i, j-1, '<', 1))
		if j < m-1 and consecutive_steps >= min_consecutive_steps:
			neighbours.append((i, j+1, '>', 1))
		if i > 0 and consecutive_steps < max_consecutive_steps:
			neighbours.append((i-1, j, '^', consecutive_steps+1))
	return neighbours

print(f"The grid is {n}x{m}")

processed = set()
remaining = SortedList()
distance = dict()

remaining.add((0,0,0,'X', 0)) # (distance[(i,j, path)], i, j, path)


min_dist = None

while len(remaining) > 0:
	d, i, j, direction, consecutive_steps = remaining[0]
	del remaining[0]
	if (i, j, direction, consecutive_steps) in processed:
		continue

	distance[(i, j, direction, consecutive_steps)] = d
	processed.add((i, j, direction, consecutive_steps))

	if i == n-1 and j == m-1:
		min_dist = d
		break

	neighbours = get_neighbours(i, j, direction, consecutive_steps)
	for ni, nj, ndir, ncons in neighbours:
		if (ni, nj, ndir, ncons) in processed:
			continue
		nd = distance.get((ni, nj, ndir, ncons), 2**32)
		if nd > d + int(grid[ni][nj]):
			distance[(ni, nj, ndir, ncons)] = d + int(grid[ni][nj])
			remaining.add((d + int(grid[ni][nj]), ni, nj, ndir, ncons))

print(min_dist)





