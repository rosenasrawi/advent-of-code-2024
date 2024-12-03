from _getinput import *

# --- Day 2: Red-Nosed Reports ---

def run_tests(rep):
    increase = all(x < y for x, y in zip(rep, rep[1:]))
    decrease = all(x > y for x, y in zip(rep, rep[1:]))
    valid = all(1 <= abs(x - y) <= 3 for x, y in zip(rep, rep[1:]))

    return increase and valid or decrease and valid

def dampener(rep):
    i = 0
    while True:
        rep_copy = rep.copy()
        rep_copy.pop(i)

        if run_tests(rep_copy):
            return True
        if i == len(rep) - 1:
            return False
        i += 1

def safety_check(reports, dampen = False):
    safe_reports = 0

    for rep in reports:
        if run_tests(rep):
            safe_reports += 1
        else: 
            if dampen:
                if dampener(rep):
                    safe_reports += 1

    return safe_reports

data = getinput('02', example=False)
reports = [list(map(int, line.split())) for line in data]

print('Part 1:', safety_check(reports, dampen=False))
print('Part 2:', safety_check(reports, dampen=True))