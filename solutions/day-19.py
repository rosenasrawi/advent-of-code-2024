from _getinput import *

# --- Day 19: Linen Layout ---

data = getinput('19', example=False)

towels = data.pop(0).split(', ')
designs = data[1:]
possible = 0

for design in designs:

    selection = [towel for towel in towels if towel in design]
    queue = selection.copy()

    while queue:
        combo = queue.pop()
        if combo != design[:len(combo)]: 
            continue

        for towel in selection:
            next_combo = combo + towel

            if next_combo != design[:len(next_combo)]: 
                continue

            if len(next_combo) > len(design):
                continue

            if next_combo == design:
                possible += 1
                queue.clear()
                break

            queue.append(next_combo)

print('Part 1:', possible)