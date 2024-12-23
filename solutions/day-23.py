from _getinput import *

# --- Day 23: LAN Party ---

data = getinput('23', example=False)
data = [tuple(map(str,line.split('-'))) for line in data]

connections = dict()
for k, v in data:
    if k in connections:
        connections[k].append(v)
    else:
        connections[k] = [v]

    if v in connections:
        connections[v].append(k)
    else:
        connections[v] = [k]

computers = set(connections.keys())

trios = set()

for computer in computers:

    for con in connections[computer]:
        inter = [computer, con]

        for next in connections[con]:

            if next not in inter:
                if next in connections[computer]:
                    trio = inter.copy()
                    trio.append(next)
                    trio = tuple(sorted(trio))

                    if any ([c[0] == 't' for c in trio]):
                        trios.add(trio)

print(len(trios))

