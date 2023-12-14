
def find_first_and_last_digits(input_string):
    digit_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    first = None
    first_pos = None
    last = None
    last_pos = None
    for spelled_digit, numerical_digit in digit_mapping.items():
    	for digit in [spelled_digit, numerical_digit]:
	    	first_idx = input_string.find(digit)
	    	last_idx = input_string.rfind(digit)
	        if first_idx >= 0 and (first_pos == None or first_idx < first_pos):
	        	first_pos = first_idx
	        	first = numerical_digit # always to the numerical value of the digit
	        if last_idx >= 0 and (last_pos == None or last_idx > last_pos):
	        	last_pos = last_idx
	        	last = numerical_digit
    
    return first + last


with open('./input/1.txt') as f:
	lines = [line.rstrip() for line in f]
	total_sum = 0
	for line in lines:
		calibration_value = find_first_and_last_digits(line)
		total_sum += int(calibration_value)
	print(total_sum)
	

