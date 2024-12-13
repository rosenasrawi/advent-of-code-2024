from _getinput import *
import regex as re

# --- Day 13: Claw Contraption ---

data = getinput('13', example=False)

def get_machines(data):

    A, B, prize = [], [], []

    for line in data:
        nums = list(map(int,re.findall(r'(\d+)', line)))
        
        if 'A' in line:
            A.append(nums)
        elif 'B' in line:  
            B.append(nums)
        elif 'Prize' in line:
            prize.append(nums)

    return list(zip(A, B, prize))

def calc_tokens(a, b, p, conversion = 0):
    tokens = 0
    ax, ay = a
    bx, by = b
    px, py = p

    px += conversion
    py += conversion

    a = round((py / by - px / bx) / (ay / by - ax / bx))
    b = round((px - a * ax) / bx)

    if a * ax + b * bx == px and a * ay + b * by == py:
        tokens += 3 * a + b
    
    return tokens

win_all = 0
press_forever = 0
machines = get_machines(data)

for machine in machines:
    a, b, prize = machine

    win_all += calc_tokens(a, b, prize)
    press_forever += calc_tokens(a, b, prize, conversion=10000000000000)

print(f"Part 1: {win_all}")
print(f"Part 2: {press_forever}")