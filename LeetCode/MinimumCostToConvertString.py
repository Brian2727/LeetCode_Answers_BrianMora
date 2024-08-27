def minimumCost(source, target, original, changed, cost):
    totalCost = 0
    # creating the Graph
    graph = {}
    for index, x in enumerate(original):
        if x not in (graph):
            graph[x] = []
            graph[x].append((changed[index], cost[index]))
        else:
            graph[x].append((changed[index], cost[index]))
    def dijkstra(c):
        # this algorith return a dictionary with the shortest path to every node form the desired node
        heap = [(c, 0)]
        lowestCostMap = {}
        while heap:
            node, cost = heap.pop()
            if node in lowestCostMap:
                if lowestCostMap[node] > cost:
                    lowestCostMap[node] = cost
                else:
                    continue
            else:
                lowestCostMap[node] = cost
            for node, c in graph[node]:
                heap.append((node, cost + c))
        return lowestCostMap
    shortest_paths = {c: dijkstra(c) for c in source}
    print(shortest_paths)
    for index, c in enumerate(source):
        if c != target[index]:
            if target[index] not in shortest_paths[c]:
                return -1
            totalCost += shortest_paths[c][target[index]]

    return totalCost