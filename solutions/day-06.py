from _getinput import *
import regex as re

# --- Day 6: Guard Gallivant ---

data = getinput(day='06', example = False)

def find_guard(data):
    for i, line in enumerate(data):
        if '^' in line:
            return (i, line.index('^'), '^')

directions = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}
dirchange = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

x, y, guard = find_guard(data)
dx, dy = directions[guard]
steps = 1

while True:
    if x+dx < 0 or x+dx > len(data)-1 or y+dy < 0 or y+dy > len(data[0])-1:
        break

    if data[x+dx][y+dy] == '#':
        guard = dirchange[guard]
        dx, dy = directions[guard]
    
    x+=dx; y+=dy

    if data[x][y] == '.':
        steps+=1
    data[x] = data[x][:y] + 'o' + data[x][y+1:]

print(steps) 












# def find_obstructions(data):
#     obstructions = []
#     for i, line in enumerate(data):
#         obs = [o.start() for o in re.finditer(r'#', line)]
#         for o in obs:
#             obstructions.append((i, o))

#     return obstructions

# obstructions = find_obstructions(data)