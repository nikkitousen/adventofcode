from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file")

args = parser.parse_args()

filepath = args.file
with open(filepath) as f:
	lines = [line.rstrip() for line in f]

steps = lines[0].split(',')
print(f"There are {len(steps)} steps")

def calc_hash(string):
	h = 0
	for c in string:
		h = ((h + ord(c)) * 17) % 256
	return h

boxes = [[] for _ in range(256)]

for step in steps:
	label, operation, focal_length = (None,None,None)
	if step[-1] == '-':
		label = step[:-1]
		operation = '-'
	else:
		label, focal_length = step.split('=')
		operation = '='
	box_number = calc_hash(label)
	box = boxes[box_number]

	idx = None
	for i in range(len(box)):
		if box[i][0] == label:
			idx = i
			break

	if operation == '=' and idx == None:
		box.append([label, focal_length])
	elif operation == '=' and idx != None:
		box[idx][1] = focal_length
	elif operation == '-' and idx != None:
		del box[idx]

total = 0
for i in range(len(boxes)):
	for j in range(len(boxes[i])):
		total += (i + 1) * (j + 1) * int(boxes[i][j][1])

print(total)
