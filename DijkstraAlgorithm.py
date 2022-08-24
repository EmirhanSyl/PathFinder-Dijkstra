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

    print(graph[(7, 8)])

    neighborNodes = {v: {} for v in nodes}
    print("--------------------------------------")
    print('\033[1;31mInitializing Node Paths... \033[0;0m')
    print("Initiated Min. Lengths Dict: ", pathLengths)
    print("Initiated Neighbors Dict:", neighborNodes)
    print("--------------------------------------")
    print()

    print("--------------------------------------")
    print('\033[1;31mDetecting Neighbors of Nodes...\033[0;0m')
    for (u, v), w_uv in graph.items():
        neighborNodes[u][v] = w_uv
        print(neighborNodes)
        neighborNodes[v][u] = w_uv
        print(neighborNodes)
        print()
    else:
        print("Neighbors of Nodes Detected!")
        print(neighborNodes)
        print("--------------------------------------")

    print('\033[1;31mSorting Nodes...\033[0;0m')
    temporaryNodes = [v for v in nodes]
    while len(temporaryNodes) > 0:
        upperBounds = {v: pathLengths[v] for v in temporaryNodes}
        print("Working Dict: ", upperBounds)
        u = min(upperBounds, key=upperBounds.get)
        print(str(u) + ". Element from working dict removed from the list due to minimum value reached")
        temporaryNodes.remove(u)

        print(neighborNodes[u])
        for v, w_uv in neighborNodes[u].items():
            pathLengths[v] = min(pathLengths[v], pathLengths[u] + w_uv)
            print(pathLengths)
        print()
    else:
        print("----------------------------------")
        print()
        print('\033[1;32mSorting Completed! Closest Paths Found: ', pathLengths)
        for key, value in pathLengths.items():
            print("From: 0, " + "To: " + str(key) + " Distance: " + str(value))





if __name__ == "__main__":
    Dijkstra(graph, nodes, 0)