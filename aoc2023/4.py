with open('./input/4.txt') as f:
	lines = [line.rstrip() for line in f]
	total = 0
	copies = [1 for _ in lines]
	for line in lines:
		winning_string, have_str = line.split('|')
		_, winning_string = winning_string.split(':')
		winning_nums = set(winning_string.split())
		my_nums = have_str.split()
		matches = list(filter(lambda x: x in winning_nums, my_nums))

		copies_of_this = copies[0]
		total += copies_of_this
		del copies[0]
		for i in range(len(matches)):
			if i < len(copies):
				copies[i] += copies_of_this

	print(total)
