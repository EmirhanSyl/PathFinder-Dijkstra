import math

nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8]

graph = {(0, 1): 4, (0, 2): 8,
         (1, 2): 11, (1, 3): 8,
         (2, 4): 7, (2, 5): 1,
         (3, 4): 2, (3, 6): 7, (3, 7): 4,
         (4, 5): 6,
         (5, 7): 2,
         (6, 7): 14, (6, 8): 9,
         (7, 8): 10}

def Dijkstra(graph, nodes, source):
    pathLengths = {v: math.inf for v in nodes}
    pathLengths[source] = 0

    neighborNodes = {v: {} for v in nodes}

    for (u, v), val in graph.items():
        neighborNodes[u][v] = val
        neighborNodes[v][u] = val

    temporaryNodes = [v for v in nodes]
    while len(temporaryNodes) > 0:
        upperBounds = {v: pathLengths[v] for v in temporaryNodes}
        u = min(upperBounds, key=upperBounds.get)

        temporaryNodes.remove(u)

        for v, val in neighborNodes[u].items():
            pathLengths[v] = min(pathLengths[v], pathLengths[u] + val)
    else:
        print()
        print('\033[1;32mSorting Completed! Closest Paths Found: ', pathLengths)
        for key, value in pathLengths.items():
            print("From: " + str(source) + " To: " + str(key) + " Distance: " + str(value))


if __name__ == "__main__":
    Dijkstra(graph, nodes, 0)