from _getinput import *

# --- Day 12: Garden Groups ---

data = getinput('12', example=False)
marked = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
adjacent = [(0, 1), (1, 0), (0, -1), (-1, 0),(-1,-1),(1,1),(-1,1),(1,-1)]
surround = {
    'tl': [(0,-1),(-1,-1), (-1,0)],
    'tr': [(-1,0),(-1,1), (0,1)],
    'bl': [(0,1), (1,1), (1,0)],
    'br': [(1,0), (1,-1), (0,-1)],
}

def out_of_bounds(x, y):
    return x < 0 or x >= len(data) or y < 0 or y >= len(data[0])

def find_corners(perimeter):
    sides = 0

    for x, y in perimeter:
        point = data[x][y]

        for key in surround:
            sur = ''
            for i, j in surround[key]:
                xi, yj = x+i, y+j
                sur += data[xi][yj] if not out_of_bounds(xi, yj) else '.'

            inner = sur[0] != point and sur[2]!= point
            outer = sur[1] != point and sur[0] == point and sur[2] == point

            sides += sum([inner, outer])

    return sides

price = 0
discount = 0

for i in range(len(data)):
    for j in range(len(data[0])):

        if marked[i][j]:
            continue

        sides = set()
        perimeter, area = 0, 0
        queue = [(i, j)]

        while queue:
            x, y = queue.pop()
            plant = data[x][y]
            marked[x][y] = 1
            area += 1

            for di, dj in adjacent:
                ni, nj = x + di, y + dj
                
                if out_of_bounds(ni, nj) or data[ni][nj] != plant:
                    sides.add((x,y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if out_of_bounds(nx, ny) or data[nx][ny] != plant:
                    perimeter+=1
                    continue

                if marked[nx][ny] or (nx, ny) in queue:
                    continue

                queue.append((nx, ny))

        corners = find_corners(sides)
        price += area * perimeter
        discount += area * corners

print('Part 1:', price)
print('Part 2:', discount)