from _getinput import *

# --- Day 10: Hoof It ---

data = getinput('10', example=False)

trailhead = []

for x,line in enumerate(data):
    for y,char in enumerate(line):
        if char == '0':
            trailhead.append([x,y])

directions = ((-1,0), (1,0), (0,-1), (0,1))

def out_of_bounds(x,y):
    return not (0 <= x < len(data) and 0 <= y < len(data[0]))

def trail_search(trail, distinct = False):
    queue, visited = [trail], []
    score = 0

    while queue:
        x,y = queue.pop(0)
        visited.append((x,y))
        prev = int(data[x][y])

        for dx,dy in directions:
            nx, ny = x+dx, y+dy

            if out_of_bounds(nx,ny) or (nx,ny) in visited:
                continue

            next = int(data[nx][ny])

            if next-prev == 1:

                if next == 9:
                    if not distinct:
                        visited.append((nx,ny))
                    score+=1
                    continue

                queue.append((nx,ny))

    return score

total, total_dist = 0,0

for trail in trailhead:
    total += trail_search(trail)
    total_dist += trail_search(trail, True)

print('Part 1:', total)
print('Part 2:', total_dist)