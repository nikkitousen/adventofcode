import re
import copy
from sortedcontainers import SortedList
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file")

args = parser.parse_args()

filepath = args.file
with open(filepath) as f:
    lines = [line.rstrip() for line in f]

empty_line_idx = lines.index('')
conditions = dict()
for cond in lines[:empty_line_idx]:
    wf_name, wf_string = re.match(r'^(\w+)\{(.*)\}$', cond).groups()
    wf_rules = wf_string.split(',')
    rules = list()
    for rule in wf_rules:
        if rule.find(':') == -1:
            rules.append([rule])
        else:
            rule_cond, rule_dest = rule.split(':')
            rule_param = rule_cond[0]
            rule_comp = rule_cond[1]
            rule_val = int(rule_cond[2:])
            rules.append([rule_param, rule_comp, rule_val, rule_dest])
    conditions[wf_name] = rules

''' 
Only for Part 2
'''

bounds = {
    'x': [1,4000],
    'm': [1,4000],
    'a': [1,4000],
    's': [1,4000],
}

def calc_combinations(bounds, wf_name):
    if wf_name == 'R':
        return 0
    if wf_name == 'A':
        result = 1
        for c in 'xmas':
            result *= (bounds[c][1]-bounds[c][0]+1)
        return result

    combinations = 0
    updated_bounds = copy.deepcopy(bounds)
    for rule in conditions[wf_name]:
        if len(rule) == 1:
            combinations += calc_combinations(copy.deepcopy(updated_bounds), rule[0])
            break
        category, condition, value, next_wf = rule
        if ((condition == '<' and updated_bounds[category][1] < value) or
            (condition == '>' and updated_bounds[category][0] > value)
        ):
            combinations += calc_combinations(copy.deepcopy(updated_bounds), next_wf)
            break
        if ((condition == '<' and updated_bounds[category][0] >= value) or
            (condition == '>' and updated_bounds[category][1] <= value)
        ):
            continue

        new_bounds = copy.deepcopy(updated_bounds)
        if condition == '<':
            new_bounds[category][1] = value-1
            updated_bounds[category][0] = value
        else:
            new_bounds[category][0] = value+1
            updated_bounds[category][1] = value
        combinations += calc_combinations(new_bounds, next_wf)
        
        
    return combinations

print(calc_combinations(bounds, 'in'))

''' 
Only for Part 1
'''

# parts = list()
# for part_str in lines[empty_line_idx+1:]:
#   part_categories = part_str[1:-1].split(',')
#   part = {
#       'x': int(part_categories[0][2:]),
#       'm': int(part_categories[1][2:]),
#       'a': int(part_categories[2][2:]),
#       's': int(part_categories[3][2:]),
#   }
#   parts.append(part)

# def follow_wf(part, wf_name):
#   if wf_name in ['A', 'R']:
#       return wf_name
#   for rule in conditions[wf_name]:
#       if len(rule) == 1:
#           return follow_wf(part, rule[0])
#       if ((rule[1] == '<' and part[rule[0]] < rule[2]) or
#           (rule[1] == '>' and part[rule[0]] > rule[2])
#       ):
#           return follow_wf(part, rule[3])

# total = 0
# for part in parts:
#   verdict = follow_wf(part, 'in')
#   print(part, end=' ')
#   print(verdict)
#   if verdict == 'A':
#       total += part['x']+part['m']+part['a']+part['s']

# print(total)


