from _getinput import * 
import re

# --- Day 3: Mull It Over ---

data = getinput('03', example=False)
if isinstance(data, list):
    data = ''.join(data)

# Part 1

mults = re.compile(r'mul\((\d+),(\d+)\)')
mults = mults.findall(data)

total = 0
for x, y in mults:
    total += int(x) * int(y)

print('Part 1:', total)

# Part 2

pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
mults = re.findall(pattern, data)

do = True; total = 0

for inst in mults:
    if inst == "don't()": do = False
    elif inst == "do()": do = True

    if do and 'mul' in inst:
        x, y = map(int, re.findall(r'\d+', inst))
        if do: total += x * y

print('Part 2:', total)