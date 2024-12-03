from _getinput import *
from collections import Counter

# --- Day 1: Historian Hysteria ---

data = getinput('01', example=False)
left, right = zip(*[map(int, line.split()) for line in data])

# Part 1
distance = [abs(a - b) for a, b in zip(sorted(left), sorted(right))]
print('Part 1:', sum(distance))

# Part 2
counted = Counter(right)
similarity = 0
for num in left:
    similarity += num * counted[num]

print('Part 2:', similarity)