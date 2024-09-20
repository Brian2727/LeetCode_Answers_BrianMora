def maxProbability(self, n, edges, succProb, start_node,
                   end_node):
    prob = 0
    curr_max = 0

    for index, edge in enumerate(edges):
        if edge[0] == start_node:
            prob = succProb[index]
            pass
        if edge[1] == end_node:
            if curr_max < prob:
                curr_max = prob
            pass
        prob = prob * succProb[index]

    return curr_max
