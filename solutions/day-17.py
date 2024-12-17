from _getinput import *
import regex as re

# --- Day 17: Chronospatial Computer ---

data = getinput('17', example=False)

def parse(data):
    register, program = [], []

    for line in data:
        nums = re.findall(r'(\d+)', line)
        if 'Register' in line:
            register.append(int(nums[0]))
        if 'Program' in line:
            program = list(map(int, nums))

    register = dict(zip('ABC', register))

    return register, program

def get_combo(operand):
    combo = {4: 'A', 5: 'B', 6: 'C'}

    if operand in combo:
        operand = register[combo[operand]]

    return operand

def run_program(register,progam):
    i = 0
    output = ''

    while True:
        if i > len(program)-1:
            break
        
        opcode = program[i]
        operand = program[i+1]

        if opcode == 0:
            register['A'] //= 2**get_combo(operand)
        elif opcode == 1:
            register['B'] ^= operand
        elif opcode == 2:
            register['B'] = get_combo(operand) % 8
        elif opcode == 3:
            if register['A'] != 0:
                i = operand
            else: i += 2
            continue
        elif opcode == 4:
            register['B'] ^= register['C']
        elif opcode == 5:
            output += str(get_combo(operand) % 8)
        elif opcode == 6:
            register['B'] = register['A'] // 2**get_combo(operand)
        elif opcode == 7:
            register['C'] = register['A'] // 2**get_combo(operand)
        
        i += 2

    return ','.join(output)

register, program = parse(data)
output = run_program(register, program)
print('Part 1:', output)

d = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] 
id = len(d)

while True:
    # Convert to base 10
    A = sum(d[i]*8**(i) for i in range(len(d)))

    register = {'A': A, 'B': 0, 'C': 0}
    output = run_program(register,program)
    output = list(map(int,output.split(',')))

    if output == program:
        break

    # One number correct, move one
    if output[id:] == program[id:]:
        id -= 1
    # Haven't found? Reset, move back
    else:
        if d[id] == 7:
            d[id] = 0
            id += 1
        # Try next number
        else:
            d[id] += 1

print('Part 2:', A)