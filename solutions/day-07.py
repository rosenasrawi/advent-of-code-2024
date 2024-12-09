from _getinput import *
import regex as re

# --- Day 7: Bridge Repair ---

data = getinput('07', example=False)

def check_valid(result, values, canconcat = False):

    val, rest = values[0], values[1:]

    if len(rest) == 1:
        if result == val+rest[0]:
            return True
        elif result == val*rest[0]:
            return True
        
        if canconcat:
            if result == int(str(val)+str(rest[0])):
                return True
    
    elif len(rest) > 1:
        plus = [val+rest[0]]+rest[1:]
        times = [val*rest[0]]+rest[1:]

        concat = int(str(val)+str(rest[0]))
        concat = [concat]+rest[1:]

        if canconcat:
            if check_valid(result, plus, canconcat) or check_valid(result, times, canconcat) or check_valid(result, concat, canconcat):
                return True
        else:
            if check_valid(result, plus) or check_valid(result, times):
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
