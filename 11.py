from collections import deque
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file")

args = parser.parse_args()

filepath = args.file
with open(filepath) as f:
	lines = [line.rstrip() for line in f]

# for line in lines:
# 	print(line)

n = len(lines)
m = len(lines[0])

galaxies = []

for i in range(n):
	for j in range(m):
		if lines[i][j] == '#':
			galaxies.append((i,j))
ng = len(galaxies)


empty_i = []
for i in range(n):
	empty = True
	for j in range(m):
		if lines[i][j] != '.':
			empty = False
			break
	if empty:
		empty_i.append(i)

empty_j = []
for j in range(m):
	empty = True
	for i in range(n):
		if lines[i][j] != '.':
			empty = False
			break
	if empty:
		empty_j.append(j)

total_dist = 0
for x in range(ng):
	for y in range(x+1, ng):
		g1 = galaxies[x]
		g2 = galaxies[y]
		ei = 0
		for i in empty_i:
			if i > min(g1[0],g2[0]) and i < max(g1[0],g2[0]):
				ei += 1
		ej = 0
		for j in empty_j:
			if j > min(g1[1],g2[1]) and j < max(g1[1],g2[1]):
				ej += 1
		dist = abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]) + (ei + ej) * 999999
		# print(f"{g1} - {g2}: {dist}")
		total_dist += dist

print(total_dist)