from _getinput import *
from itertools import combinations as comb

# --- Day 8: Resonant Collinearity ---

data = getinput('08', example=False)
data = [list(map(str, line)) for line in data]

def find_antennae(data):
    antennae = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char != '.':
                antennae.setdefault(char, []).append((x, y))
    return antennae

antennae = find_antennae(data)

def inbound(data, x, y):
    return 0 <= x < len(data[0]) and 0 <= y < len(data)

def gen_antinodes(data, antennae):
    freq = list(antennae.keys())
    antinodes = 0

    for f in freq:
        for combo in comb(antennae[f], 2):
            (ax, ay), (bx, by) = combo
            dx, dy = ax - bx, ay - by
        
            cx, cy = ax + dx, ay + dy
            dx, dy = bx - dx, by - dy

            for x, y in [(cx, cy), (dx, dy)]:
                if inbound(data, x, y) and data[y][x] != '#':
                    data[y][x] = '#'
                    antinodes += 1

    return antinodes

antinodes = gen_antinodes(data, antennae)
print('Part 1,', antinodes)