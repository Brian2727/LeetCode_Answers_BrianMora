def ViewFromRigthSide(tree):
    queue = []
    res   = []
    depth = 0
    counterSeenNodes = 0
    temp = tree.root
    queue.append(tree.root)
    nodesOnDepth = len(queue)
    while len(queue) > 0:
        if counterSeenNodes == nodesOnDepth:
            counterSeenNodes = 0
            nodesOnDepth = len(queue)
            depth += 1
            res.append(temp.value)
        temp = queue.pop(0)
        counterSeenNodes += 1
        print(f'looking at node {temp.value} this is node number {counterSeenNodes} current depth {depth} numNode on this depth {nodesOnDepth}')
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
    res.append(temp.value)
    print(f'Max depth is {depth} and the nodes we can see from rigth are {res}')