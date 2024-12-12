from _getinput import *
import regex as re

# --- Day 11: Plutonian Pebbles ---

data = getinput('11', example=True)
stones = re.findall(r'\d+', data)

def split_stone(stone):
    if stone == '0':
        return '1'
    
    if len(stone) % 2 == 0:
        left = stone[:len(stone)//2]
        right = stone[len(stone)//2:]

        right = right.lstrip('0') or '0'

        return f'{left} {right}'

    return str(int(stone)*2024)

for i in range(25):
    stones = re.findall(r'\d+', data)
    blink = ''

    for i, stone in enumerate(stones):

        stone = split_stone(stone)
        blink += stone + ' '
        
    data = blink

stones = re.findall(r'\d+', data)
print('Part 1:', len(stones))