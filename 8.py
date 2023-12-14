from collections import deque

def follow_instructions(graph, instructions, starting_node):
	current_node = starting_node
	for d in instructions:
		current_node = graph[current_node][d]
	return current_node

def repeat_instructions(graph, starting_nodes):
	new_nodes = []
	for node in starting_nodes:
		new_nodes.append(graph[node])
	return new_nodes

def is_ending_position(nodes):
	for node in nodes:
		if node[-1] != 'Z':
			return False
	return True


with open('./8.txt') as f:
	lines = [line.rstrip() for line in f]

instructions = lines[0]
graph = {}
current_nodes = []
for line in lines[2:]:
	node = line[:3]
	left = line[7:10]
	right = line[12:15]
	graph[node] = {
		'L': left,
		'R': right
	}
	if node[-1] == 'A':
		current_nodes.append(node)

new_graph = {}
for node in graph.keys():
	new_graph[node] = follow_instructions(graph, instructions, node)

a_nodes = []
for node in new_graph.keys():
	if node[-1] == 'A':
		a_nodes.append(node)

a_steps = {}

for n in a_nodes:
	a_steps[n] = []
	current_node = n
	times_reached_z = 0
	steps = 0
	while times_reached_z < 1:
		current_node = new_graph[current_node]
		steps += 1
		if current_node[-1] == 'Z':
			a_steps[n].append(steps)
			times_reached_z += 1

print(a_steps)

# Turns out all cycles start in the Z node. Hence we need the LCM
# of the sizes of these cycles, and multiply it by the len of the instructions

print(56787204941 * len(instructions))




