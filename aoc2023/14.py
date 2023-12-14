from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file")

args = parser.parse_args()

filepath = args.file
with open(filepath) as f:
	board = [line.rstrip() for line in f]

n = len(board)
m = len(board[0])

def tilt_north(board):
	new_board = ['' for _ in range(n)]
	for j in range(m):
		position_to_slide = 0
		for i in range(n):
			if board[i][j] == 'O':
				new_board[position_to_slide] += 'O'
				position_to_slide += 1
			elif board[i][j] == '#':
				for ii in range(position_to_slide, i):
					new_board[ii] += '.'
				new_board[i] += '#'
				position_to_slide = i+1
			if i == n-1 and position_to_slide < n:
				for ii in range(position_to_slide, n):
					new_board[ii] += '.'
	return new_board

def rotate_right(board):
	new_board = ['' for _ in range(n)]
	for j in range(m):
		for i in range(n):
			new_board[j] += board[n-1-i][j]
	return new_board

def calculate_score(board):
	total = 0
	for i in range(n):
		for j in range(m):
			if board[i][j] == 'O':
				total += n-i
	return total

def print_board(board):
	for line in board:
		print(line)

seen = dict()
target_cycle = None
for cycle in range(1, 1000):
	for _ in range(4):
		board = tilt_north(board)
		board = rotate_right(board)
	
	board_hash = hash(tuple(board))
	if board_hash in seen.keys() and target_cycle == None:
		first_of_cycle = seen[board_hash]
		size_of_cycle = cycle - first_of_cycle
		target_cycle = (10**9 - first_of_cycle) % size_of_cycle + first_of_cycle + size_of_cycle
		# print(f"Iteration {cycle} seen before at {seen[board_hash]} ", end='')
		# print(f"- Score: {calculate_score(board)}")
	else:
		seen[board_hash] = cycle

	if cycle == target_cycle:
		break

print(calculate_score(board))