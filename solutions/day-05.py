from _getinput import *

# --- Day 5: Print Queue ---

data = getinput(day='05', example = False)

rules, pages = [], []

for line in data:
    if '|' in line:
        rules.append(line)
    elif ',' in line:
        pages.append(list(map(int,line.split(','))))

def page_valid(page):

    ids = list(range(len(page)))

    for i in ids:
        rest = ids.copy(); rest.pop(i)
        comb = [sorted([i,r]) for r in rest]

        for l,r in comb:
            if not f'{page[l]}|{page[r]}' in rules:
                page[l], page[r] = page[r], page[l]
                page_valid(page)
                return page
    
    return True

correct, incorrect = 0, 0

for page in pages:

    valid = page_valid(page)

    if valid == True: 
        correct += page[len(page) // 2]
    else:
        incorrect += valid[len(valid) // 2]

print('Part 1:', correct)
print('Part 2:', incorrect)