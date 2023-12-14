from collections import deque
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file")

args = parser.parse_args()

filepath = args.file
with open(filepath) as f:
	lines = [line.rstrip() for line in f]

for line in lines:
	print(line)


pipe_to_neighbors = {
	'|': [[-1, 0], [1, 0]],
	'-': [[0, -1], [0, 1]],
	'J': [[-1, 0], [0, -1]],
	'L': [[-1, 0], [0, 1]],
	'7': [[0, -1], [1, 0]],
	'F': [[0, 1], [1, 0]],
}

n = len(lines)
m = len(lines[0])
neighbors = dict()

for i in range(n):
	for j in range(m):
		neighbors[(i,j)] = set()

def in_bounds(i, j):
	return i >= 0 and i < n and j >= 0 and j < m

def add_neighbors(i, j):
	pipe = lines[i][j]
	if pipe not in pipe_to_neighbors.keys():
		return
	for di, dj in pipe_to_neighbors[pipe]:
		if in_bounds(i+di, j+dj):
			neighbors[(i,j)].add((i+di, j+dj))
			if lines[i+di][j+dj] == 'S':
				neighbors[(i+di, j+dj)].add((i,j))


s = None
for i in range(n):
	for j in range(m):
		pipe = lines[i][j]
		if pipe == 'S':
			s = (i,j)
		else:
			add_neighbors(i, j)

q = deque([s])
loop = set()
while len(q) > 0:
	current_node = q.popleft()
	loop.add(current_node)
	for node in neighbors[current_node]:
		if node not in loop:
			q.append(node)
			loop.add(node)

print(loop)

nn = 2*n+1
mm = 2*m+1
inflated = []

def get_original(ii, jj):
	return (int((ii-1)/2), int((jj-1)/2))

inflated_empty = '*'
for ii in range(nn):
	row = ''
	for jj in range(mm):
		if ii == 0 or ii == nn-1:
			row += inflated_empty
		elif jj == 0 or jj == mm-1:
			row += inflated_empty
		elif ii % 2 == 0 and jj % 2 == 0:
			row += inflated_empty
		elif ii % 2 == 1 and jj % 2 == 1:
			(i,j) = get_original(ii,jj)
			if (i,j) in loop:
				row += lines[i][j]
			else:
				row += '.'
		elif ii % 2 == 1 and jj % 2 == 0:
			(li, lj) = get_original(ii, jj-1)
			(ri, rj) = get_original(ii, jj+1)
			if (li, lj) in loop and (ri, rj) in loop and (li, lj) in neighbors[(ri,rj)]:
				row += '-'
			else:
				row += inflated_empty
		else: # ii % 2 == 0 and jj % 2 == 1
			(ui, uj) = get_original(ii-1, jj)
			(di, dj) = get_original(ii+1, jj)
			if (ui, uj) in loop and (di, dj) in loop and (ui, uj) in neighbors[(di,dj)]:
				row += '|'
			else:
				row += inflated_empty
	inflated.append(row)


for line in inflated:
	print(line)


def in_bounds_inflated(ii, jj):
	return ii >= 0 and ii < nn and jj >=0 and jj < mm

q = deque([(0,0)])
outside = set()
while len(q) > 0:
	(ii,jj) = q.popleft()
	outside.add((ii,jj))
	inflated[ii] = inflated[ii][:jj] + ' ' + inflated[ii][jj+1:]
	diff_i = [-1, 0, 1, 0]
	diff_j = [0, -1, 0, 1]
	for di, dj in zip(diff_i, diff_j):
		xii = ii+di
		xjj = jj+dj
		if in_bounds_inflated(xii, xjj) and inflated[xii][xjj] in ['.', inflated_empty] and not (xii, xjj) in outside:
			q.append((xii,xjj))
			outside.add((xii, xjj))

for line in inflated:
	print(line)

print(len(outside))


inside_count = 0
for ii in range(nn):
	for jj in range(mm):
		if inflated[ii][jj] == '.':
			inside_count += 1

print(inside_count)




# for i in range(n):
# 	for j in range(m):
# 		print(f"{(i,j)}: {neighbors[(i,j)]}")


