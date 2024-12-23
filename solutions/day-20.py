from _getinput import *

# --- Day 20: Race Condition ---

data = getinput('20', example=False)
data = [list(line) for line in data]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
walls = []

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == 'S':
            start = (x, y)
        if char == 'E':
            end = (x, y)
            
def bfs(start, end, data):
    queue = [(start)]
    visited = set()
    path = []
    
    while queue:
        x, y = queue.pop(0)
        visited.add((x, y))
        path.append((x, y))
        
        if (x, y) == end:
            return path
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if (nx, ny) in visited:
                continue
            if data[ny][nx] == '#':
                continue
            queue.append(((nx, ny)))
            
    return -1

path = bfs(start, end, data)
around = set()

for dx in range(-20, 21):
    for dy in range(-20, 21):
        if dx == 0 and dy == 0:
            continue
        if abs(dx) + abs(dy) <= 20:
            around.add((dx, dy))

distances = dict()

for dist, (x,y) in enumerate(path):
    distances[(x,y)] = dist

cheat = 0
mega_cheat = 0
path = set(path)

for (x,y) in path:

    target = distances[(x,y)]
    if target <= 100:
        continue

    for dx,dy in around:
        nx, ny = x+dx, y+dy

        if (nx,ny) in path:
            new_d = distances[(nx,ny)] + abs(dx) + abs(dy)
            if new_d < target:
                short = target - new_d
                if short >= 100:
                    mega_cheat+=1
                    if abs(dx) + abs(dy) <= 2:
                        cheat+=1

print('Part 1:', cheat)
print('Part 2:', mega_cheat)