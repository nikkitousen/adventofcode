with open('./input/2.txt') as f:
	lines = [line.rstrip() for line in f]
	# sum_of_possible_ids = 0
	sum_of_powers = 0
	for line in lines:
		game_id_str, reveals_str = line.split(':')
		_, game_id = game_id_str.split()
		reveals = reveals_str.split(';')
		min_values = {
			'red': 0,
			'blue': 0,
			'green': 0
		}
		for reveal in reveals:
			color_reveals = [r.lstrip() for r in reveal.split(',')]
			for color_reveal in color_reveals:
				amount, color = color_reveal.split()
				min_values[color] = max(min_values[color], int(amount))

		sum_of_powers += min_values['red'] * min_values['green'] * min_values['blue']
		# if (min_values['red'] <= 12 and min_values['green'] <= 13 and min_values['blue'] <= 14):
		# 	sum_of_possible_ids += int(game_id)

	# print(sum_of_possible_ids)
	print(sum_of_powers)



