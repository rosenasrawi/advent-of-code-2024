from _getinput import *

# --- Day 16: Reindeer Maze ---

data = getinput('16', example=False)

def get_grid(data):
    grid = [list(map(str, line)) for line in data]

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == 'S':
                start = (x, y)
            if char == 'E':
                end = (x, y)

    return grid, start, end

directions = [(0,1), (1,0), (0,-1), (-1,0)]

def bfs(start, end):

    best_score = float('inf')
    sx, sy = start
    turn = (1,0)
    path = set()
    paths = dict()

    queue = [(sx, sy, 0, turn, path)]
    visited = dict()

    while queue:
        x, y, score, turn, path = queue.pop(0)

        if grid[y][x] == '#':
            continue

        if (x,y) == end:
            
            if score not in paths:
                paths[score] = path
            elif score in paths:
                paths[score].update(path)

            if score < best_score:
                best_score = score
            continue

        key = (x,y,turn)

        if key in visited and visited[key] < score:
            continue
        visited[key] = score

        for dx, dy in directions:

            new_turn = (dx,dy)
            new_score = score
            new_path = path.copy()

            if turn == new_turn:
                new_score += 1
            elif turn[0] == dx or turn[1] == dy:
                new_score += 2001
            else:
                new_score += 1001

            nx = x+dx
            ny = y+dy
            new_path.add((nx, ny))

            queue.append((nx, ny, new_score, new_turn, new_path))

    return best_score, len(paths[min(paths.keys())])+1

grid, start, end = get_grid(data)
total, best = bfs(start, end)

print('Part 1:', total)
print('Part 2:', best)