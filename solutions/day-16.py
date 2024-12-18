from _getinput import *
import regex as re

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

    queue = [(sx,sy,0,turn)]
    visited = dict()

    while queue:
        x, y, score, turn = queue.pop(0)

        if grid[y][x] == '#':
            continue

        if (x,y) == end:
            if score < best_score:
                best_score = score
            continue

        key = (x,y)
        if key in visited and visited[key] < score:
            continue
        visited[key] = score

        for dx, dy in directions:

            new_turn = (dx,dy)
            new_score = score

            if turn == new_turn:
                new_score += 1
            elif turn[0] == dx or turn[1] == dy:
                new_score += 2001
            else:
                new_score += 1001

            queue.append((x+dx, y+dy, new_score, new_turn))

    return best_score

grid, start, end = get_grid(data)

print('Part 1:', bfs(start,end))