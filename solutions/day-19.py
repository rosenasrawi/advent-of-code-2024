from _getinput import *

# --- Day 19: Linen Layout ---

data = getinput('19', example=False)

towels = data.pop(0).split(', ')
designs = data[1:]

def check_design(combo, design, n):
    if combo in memo:
        return memo[combo]

    if combo == design:
        return 1
    
    if len(combo) > len(design):
        return 0
    
    for towel in selection:
        next_combo = combo+towel

        if next_combo == design[:len(next_combo)]:
            n += check_design(next_combo, design, 0)
            
    memo[combo] = n
    return n

possible = 0
all_possible = 0

for design in designs:
    memo = dict()
    selection = [towel for towel in towels if towel in design]

    count = check_design('', design, 0)
    all_possible += count
    if count > 0:
        possible += 1

print(possible, all_possible)