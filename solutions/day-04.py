from _getinput import *
import regex as re

# --- Day 4: Ceres Search ---

data = getinput('04', example=False)
hlim, vlim = len(data), len(data[0])

# Part 1
def get_diag(data):

    diags = []

    for h in range(hlim):
        diagonal = ''.join(data[h-i][i] for i in range(min(h+1, vlim)))
        diags.append(diagonal)

    for v in range(1, vlim):
        diagonal = ''.join(data[hlim-i-1][v+i] for i in range(min(hlim, vlim-v)))
        diags.append(diagonal)

    return diags

vert = [''.join(data[j][i] for j in range(hlim)) for i in range(vlim)]
diag_1 = get_diag(data)

data_rot = [''.join(row) for row in zip(*data[::-1])]
diag_2 = get_diag(data_rot)

count = 0
for line in data + vert + diag_1 + diag_2:
    count += len(re.findall(r"XMAS|SAMX", line, overlapped=True))

print('Part 1:', count)

# Part 2
xmas = ['MSMS', 'SMSM', 'MMSS', 'SSMM']
count = 0

for h in range(1, hlim-1):
    for v in range(1, vlim-1):
        if data[h][v] == 'A':
            sur = data[h-1][v-1]+data[h-1][v+1]+data[h+1][v-1]+data[h+1][v+1]
            if sur in xmas:
                count+=1

print('Part 2:', count)