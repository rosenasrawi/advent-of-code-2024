from _getinput import *
import regex as re

# --- Day 7: Bridge Repair ---

data = getinput('07', example=False)

def check_valid(result, values, cct = False):

    val, rest = values[0], values[1:]

    if len(rest) == 1:
        if result in [val+rest[0], val*rest[0]]:
            return True        
        if result == int(str(val)+str(rest[0])) and cct:
            return True
    
    elif len(rest) > 1:
        plus = [val+rest[0]]+rest[1:]
        times = [val*rest[0]]+rest[1:]
        concat = [int(str(val)+str(rest[0]))]+rest[1:]

        if check_valid(result, plus, cct) or check_valid(result, times, cct):
            return True
        
        if check_valid(result, concat, cct) and cct:
            return True

total_1, total_2 = 0,0

for line in data:
    result, values = line.split(':')
    result = int(result)
    values = list(map(int, re.findall(r'\d+', values)))

    if check_valid(result, values):
        total_1 += result
    
    if check_valid(result, values, True):
        total_2 += result

print('Part 1:', total_1)
print('Part 2:', total_2)