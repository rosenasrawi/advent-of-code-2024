from _getinput import *
import networkx as nx

# --- Day 23: LAN Party ---

data = getinput('23', example=False)

def connect(data):
    data = [tuple(map(str,line.split('-'))) for line in data]
    connections = dict()

    for k, v in data:
        connections.setdefault(k, []).append(v)
        connections.setdefault(v, []).append(k)

    return connections

def find_trios(connections):
    computers = list(connections.keys())
    trios = set()

    for computer in computers:
        for con in connections[computer]:
            for next in connections[con]:

                if next != computer and computer in connections[next]:
                    trio = tuple(sorted([computer, con, next]))
                    if any(c.startswith('t') for c in trio):
                        trios.add(trio)

    return len(trios)

def find_LAN(data):
    edges = [tuple(map(str,line.split('-'))) for line in data]

    G = nx.Graph()
    G.add_edges_from(edges)

    cliques = list(nx.find_cliques(G))
    largest_clique = sorted(max(cliques, key=len))

    return ','.join(largest_clique)

connections = connect(data)

print('Part 1:', find_trios(connections))
print('Part 2:', find_LAN(data))