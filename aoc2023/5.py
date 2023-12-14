with open('./5.txt') as f:
	lines = [line.rstrip() for line in f]
	seed_info = [int(seed) for seed in lines[0][7:].split()]
	seed_ranges = list()
	seed_i = 0
	while seed_i < len(seed_info):
		# inclusive ranges
		seed_ranges.append((seed_info[seed_i], seed_info[seed_i]+seed_info[seed_i+1]-1))
		seed_i += 2
	seed_ranges.sort()

	lines = lines[2:]
	idx = 0
	while idx < len(lines):
		idx += 1
		mapping_ranges = list()
		while idx < len(lines) and lines[idx] != '':
			ds,ss,r = [int(x) for x in lines[idx].split()]
			idx += 1
			mapping_ranges.append((ss, ss+r-1, ds))
		mapping_ranges.sort()

		i=0
		j=0
		new_seed_ranges = list()
		while i < len(seed_ranges):
			if j < len(mapping_ranges):
				diff = mapping_ranges[j][2]-mapping_ranges[j][0]
				if seed_ranges[i][1] < mapping_ranges[j][0]:
					new_seed_ranges.append(seed_ranges[i])
					i += 1
				elif seed_ranges[i][0] > mapping_ranges[j][1]:
					j += 1
				elif seed_ranges[i][0] < mapping_ranges[j][0]:
					new_seed_ranges.append((seed_ranges[i][0], mapping_ranges[j][0]-1))
					seed_ranges[i] = (mapping_ranges[j][0], seed_ranges[i][1])
				elif seed_ranges[i][1] <= mapping_ranges[j][1]:
					new_seed_ranges.append((seed_ranges[i][0]+diff, seed_ranges[i][1]+diff))
					i += 1
				else: # seed_ranges[i][1] > mapping_ranges[j][1]:
					new_seed_ranges.append((seed_ranges[i][0]+diff, mapping_ranges[j][1]+diff))
					seed_ranges[i] = (mapping_ranges[j][1]+1, seed_ranges[i][1])
					j += 1
			else:
				new_seed_ranges.append(seed_ranges[i])
				i += 1
		new_seed_ranges.sort()
		seed_ranges = new_seed_ranges

		idx+=1
	print(seed_ranges)