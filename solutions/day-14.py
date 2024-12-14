from _getinput import *
import regex as re

# --- Day 14: Restroom Redoubt ---

data = getinput('14', example=False)

def parse(data):
    robots = []
    velocities = []

    max_x, max_y = 0, 0
    for line in data:
        px, py, vx, vy = map(int, re.findall(r'-?\d+', line))

        max_x = max(max_x, px)
        max_y = max(max_y, py)
        
        robots.append((px, py))
        velocities.append((vx, vy))

    return robots, velocities, max_x, max_y

def update_robots(robots, velocities):

    for i, robot in enumerate(robots):
        x, y = robot
        vx, vy = velocities[i]

        x = (x + vx) % (max_x + 1)
        y = (y + vy) % (max_y + 1)
            
        robots[i] = (x, y)

    return robots

def split_field(robots):

    q1, q2, q3, q4 = 0, 0, 0, 0
    mid_x, mid_y = max_x//2, max_y//2

    for x, y in robots:
        if x < mid_x and y < mid_y:
            q1 += 1
        elif x > mid_x and y < mid_y:
            q2 += 1
        elif x < mid_x and y > mid_y:
            q3 += 1
        elif x > mid_x and y > mid_y:
            q4 += 1

    return q1*q2*q3*q4

def place_robots(robots):

    field = [['🎄' for _ in range(max_x+1)] for _ in range(max_y+1)]
    for robot in robots:
        x, y = robot
        field[y][x] = '🎁'

    return field

def show_field(field):
    for line in field:
        print(''.join(line))

# Part 1

robots, velocities, max_x, max_y = parse(data)

for _ in range(100):
    robots = update_robots(robots, velocities)

print(f"Part 1: {split_field(robots)}")

# Part 2
robots, velocities, max_x, max_y = parse(data)
seconds, xmas = 0, False

while not xmas:
    seconds+=1
    robots = update_robots(robots, velocities)
    field = place_robots(robots)

    for line in field:
        if '🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁' in ''.join(line):
            xmas = True
            show_field(field)
            break

print(f"Part 2: {seconds}")