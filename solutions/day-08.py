from _getinput import *
from itertools import combinations as comb

# --- Day 8: Resonant Collinearity ---

data = getinput('08', example=True)

def find_antennae(data):

    antennae = {}

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char != '.':
                antennae.setdefault(char, []).append((x, y))
                
    return antennae

def inbound(data, x, y):
    return 0 <= x < len(data[0]) and 0 <= y < len(data)

def gen_antinodes(data, harmonics=False):

    antennae = find_antennae(data)
    datmap = [list(map(str, line)) for line in data]

    for positions in antennae.values():
        for combo in comb(positions, 2):
            (ax, ay), (bx, by) = combo
            dx, dy = ax - bx, ay - by

            ax += dx; ay += dy
            bx -= dx; by -= dy

            for x, y in [(ax, ay), (bx, by)]:
                if inbound(datmap, x, y) and datmap[y][x] != '#':
                    datmap[y][x] = '#'

            if harmonics:

                anti = set()
                while inbound(datmap, ax+dx, ay+dy) or inbound(datmap, bx-dx, by-dy):
                    ax += dx; ay += dy
                    bx -= dx; by -= dy
                    if inbound(datmap, ax, ay):
                        anti.add((ax,ay))
                    if inbound(datmap, bx, by):
                        anti.add((bx,by))
                    
                for x,y in anti:
                    if datmap[y][x] != '#':
                        datmap[y][x] = '#'

    if harmonics: 
        return sum(char != '.' for line in datmap for char in line)
    else:
        return sum(char == '#' for line in datmap for char in line)

print('Part 1:', gen_antinodes(data))
print('Part 2:', gen_antinodes(data, harmonics=True))