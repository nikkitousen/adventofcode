def get_adjacent_gears(lines, i, j):
	gear_positions = set()
	idx_diff = [-1, 0, 1]
	for diff_i in idx_diff:
		for diff_j in idx_diff:
			ii = i + diff_i
			jj = j + diff_j
			if ii < 0 or ii >= len(lines) or jj < 0 or jj >= len(lines[i]):
				continue
			if lines[ii][jj] == '*':
				gear_positions.add((ii,jj))
	return gear_positions

with open('./input/3.txt') as f:
	lines = [line.rstrip() for line in f]
	gear_map = {}
	for i in range(len(lines)):
		line = lines[i]
		current_num = 0
		scanning_num = False
		adjacent_gears = set()
		for j in range(len(line)):
			c = line[j]
			if c.isdigit():
				scanning_num = True
				current_num = current_num * 10 + int(c)
				gear_positions = get_adjacent_gears(lines,i,j)
				adjacent_gears.update(gear_positions)
			if scanning_num and (not c.isdigit() or j == len(line)-1):
				for gear in adjacent_gears:
					if gear not in gear_map:
						gear_map[gear] = []
					gear_map[gear].append(current_num)
				scanning_num = False
				current_num = 0
				adjacent_gears = set()

	result = 0
	for adj_list in gear_map.values():
		if len(adj_list) == 2:
			result += adj_list[0] * adj_list[1]

	print(result)


