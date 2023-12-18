from sortedcontainers import SortedList
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file")

args = parser.parse_args()

filepath = args.file
with open(filepath) as f:
	lines = [line.rstrip().split() for line in f]

wrong_steps = [(d, int(s), c[2:-1]) for d,s,c in lines]
d_map = {
	'0': 'R',
	'1': 'D',
	'2': 'L',
	'3': 'U',
}
steps = []
for ws in wrong_steps:
	s = int(ws[2][:-1], 16)
	d = d_map[ws[2][-1]]
	steps.append((d, s))

d_count = {d:0 for d in ['R', 'L', 'U', 'D']}
for step in steps:
	d_count[step[0]] += step[1]


n = d_count['R']+d_count['L']+2
m = d_count['D']+d_count['U']+2

d_diff = {
	'R': [0, 1],
	'L': [0, -1],
	'D': [1, 0],
	'U': [-1, 0],
}

i, j = d_count['U'], d_count['L']

horizontal_intervals = SortedList()
for d, s in steps:
	ni = i + d_diff[d][0]*s
	nj = j + d_diff[d][1]*s
	if d in ['R', 'L']:
		horizontal_intervals.add((i, min(j, nj), max(j, nj)))
	i = ni
	j = nj

print(f"The grid is {n}x{m}")

current_intervals = SortedList()
current_intervals_i = None
total_area = 0

idx_intervals = 0
while idx_intervals < len(horizontal_intervals):
	intervals_i = horizontal_intervals[idx_intervals][0]
	start = idx_intervals
	end = start+1
	while end < len(horizontal_intervals) and horizontal_intervals[end][0] == intervals_i:
		end += 1
	idx_intervals = end

	if current_intervals_i != None:
		for existing_interval in current_intervals:
			ej1, ej2 = existing_interval
			if ej1 == None or ej2 == None:
				continue
			total_area += (intervals_i - current_intervals_i) * (ej2 - ej1 + 1)

	current_intervals_i = intervals_i

	all_intervals = SortedList()
	for ei in current_intervals:
		eij1, eij2 = ei
		if ej1 == None or ej2 == None:
			continue
		all_intervals.add((eij1, -1 ,eij2))
	for k in range(start, end):
		_, hij1, hij2 = horizontal_intervals[k]
		all_intervals.add((hij1, 1, hij2))

	new_current_intervals = []
	merged_interval_j1 = None
	merged_interval_j2 = None

	for interval in all_intervals:
		j1, _, j2 = interval
		if merged_interval_j1 == None:
			merged_interval_j1 = j1
			merged_interval_j2 = j2
		elif j1 > merged_interval_j2 + 1:
			new_current_intervals.append((merged_interval_j1, merged_interval_j2))
			merged_interval_j1 = j1
			merged_interval_j2 = j2
		elif j1 >= merged_interval_j2:
			merged_interval_j2 = j2
		elif j1 < merged_interval_j2:
			if j1 > merged_interval_j1:
				new_current_intervals.append((merged_interval_j1, j1))
			if j1 == merged_interval_j1 and j2 == merged_interval_j2:
				total_area += j2-j1+1
				merged_interval_j1 = None
				merged_interval_j2 = None
			elif j1 == merged_interval_j1:
				total_area += j2-j1
				merged_interval_j1 = j2
			elif j2 == merged_interval_j2:
				merged_interval_j1 = None
				merged_interval_j2 = None
				total_area += j2-j1
			else:
				merged_interval_j1 = j2
				total_area += j2-j1-1
	if merged_interval_j1 != None:
		new_current_intervals.append((merged_interval_j1, merged_interval_j2))
	current_intervals = new_current_intervals.copy()

print(total_area)

