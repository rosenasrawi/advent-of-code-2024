from _getinput import *

# --- Day 9: Disk Fragmenter ---

data = getinput('09', example=False)

num, new = 0, []

for i,n in enumerate(data):
    
    if i % 2 == 0:
        new += [str(num)] * int(n)
        num += 1
    else:
        new += ['.'] * int(n)

empty = [i for i,n in enumerate(new) if n == '.']

while empty:

    if new[-1] == '.':
        new.pop()
        empty.pop()
        continue

    num = new.pop()
    id = empty.pop(0)
    new[id] = num

total = 0

for i, n in enumerate(new):
    total += i * int(n)

print('Part 1:', total)