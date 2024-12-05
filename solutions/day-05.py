from _getinput import *

# --- Day 5: Print Queue ---

data = getinput(day='05', example = False)

rules, pages = [], []

for line in data:
    if '|' in line:
        rules.append(line)
    elif ',' in line:
        pages.append(list(map(int,line.split(','))))

correct = 0

for page in pages:

    ids = list(range(len(page)))
    valid = True

    for i in ids:
        rest = ids.copy()
        rest.pop(i)

        comb = [sorted([i,r]) for r in rest]

        if not all(f'{page[l]}|{page[r]}' in rules for l,r in comb):
            valid = False
            break

    if valid: correct += page[len(page) // 2]

print('Part 1:', correct)