from _getinput import *

# --- Day 18: RAM Run ---

example = False
data = getinput('18', example)
coor = [(int(x), int(y)) for line in data for x, y in [line.split(',')]]

if example:
    grid_max, bites = 6, 12
else:
    grid_max, bites = 70, 1024

def get_grid():
    grid = [['.' for _ in range(grid_max+1)] for _ in range(grid_max+1)]
    for x, y in coor[:bites]:
        grid[y][x] = '#'
    return grid

directions = [(0,1), (1,0), (0,-1), (-1,0)]

def out_of_bounds(x, y):
    return x < 0 or x > grid_max or y < 0 or y > grid_max

grid = get_grid()
start = (0,0)
end = (grid_max, grid_max)

def bfs(end):
    queue = [(0,0,0)]
    visited = set()

    while queue:
        x, y, dist = queue.pop(0)

        if (x,y) == end:
            return dist, visited
        
        if out_of_bounds(x,y) or (x,y) in visited:
            continue

        if grid[y][x] == '#':
            continue 

        visited.add((x,y))
        for dx, dy in directions:
            queue.append((x+dx, y+dy, dist+1))

    return None, visited

steps, visited = bfs(end)

filtered_coor = [c for c in coor[bites:] if c in visited]

for x, y in filtered_coor:
    grid[y][x] = '#'
    dist, _ = bfs(end)

    if dist == None:
        blocked = f'{x},{y}'
        break

print('Part 1:', steps)
print('Part 2:', blocked)