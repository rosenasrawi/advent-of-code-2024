from _getinput import *
import regex as re

# --- Day 6: Guard Gallivant ---

data = getinput(day='06', example = False)
data = [list(map(str, line)) for line in data]

def find_guard(data):
    for i, line in enumerate(data):
        if '^' in line:
            return (i, line.index('^'), '^')

start_guard = find_guard(data)
directions = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}
dirchange = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def guard_route(data, start_guard):

    x, y, guard = start_guard
    dx, dy = directions[guard]

    route = [line.copy() for line in data]
    bumps = set()
    steps = 1

    while True:
        if not (0 <= x+dx < len(route) and 0 <= y+dy < len(route[0])):
            break

        while route[x+dx][y+dy] == '#':
            if (x,y,guard) in bumps:
                return None
            bumps.add((x,y,guard))

            guard = dirchange[guard]
            dx, dy = directions[guard]
        
        x+=dx; y+=dy

        if route[x][y] == '.':
            steps+=1
        route[x][y] = 'o'

    return route, steps

route, steps = guard_route(data, start_guard)

x, y, guard = start_guard
start = (x,y)
loopz = 0

for x, line in enumerate(route):
    for y, char in enumerate(line):

        if char == 'o' and (x,y) != start:
            data[x][y] = '#'
            collision = guard_route(data, start_guard)
            if collision is None:
                loopz+=1
            data[x][y] = '.'

print('Part 1:', steps)
print('Part 2:', loopz)