from _getinput import *
import regex as re

# --- Day 7: Bridge Repair ---

data = getinput('07', example=True)

def check_valid(result, values):

    val, rest = values[0], values[1:]

    if len(rest) == 1:
        if result in [val+rest[0], val*rest[0]]:
            return True
    
    elif len(rest) > 1:
        plus = [val+rest[0]]+rest[1:]
        times = [val*rest[0]]+rest[1:]

        if check_valid(result, plus) or check_valid(result, times):
            return True

total = 0

for line in data:
    result, values = line.split(':')
    result = int(result)
    values = list(map(int, re.findall(r'\d+', values)))

    if check_valid(result, values):
        total += result

print('Part 1:', total)
