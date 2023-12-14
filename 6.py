import math

with open('./6.txt') as f:
	lines = [line.rstrip() for line in f]

time = int(''.join((lines[0][len('Time:'):]).split()))
distance = int(''.join((lines[1][len('Distance:'):]).split()))

left = math.ceil(0.0001 + (time - math.sqrt(time**2 - 4*distance))/2)
print(time - 2*left + 1)