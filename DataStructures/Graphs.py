#first U is for Unordered second Is for NO Direction and Third is no weigth.
class Node:
    next = None
    def __init__(self,value):
        self.data = value
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.numNodes = 0

    def __init__(self,node):
        node = Node(node)
        self.head = node
        self.numNodes = 1

    def addNode(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def removeNode(self,value):
        if self.head.value == value:
            self.head = self.head.next
            return "Head removed"
        else:
            temp     = self.head
            currtemp = self.head.next
            while currtemp:

                if currtemp.value == value:
                    temp.next = currtemp.next
                    return 'removed'
                else:
                    currtemp = currtemp.next
                    temp     = temp.next
            return 'No value Found'

    def getAll(self):
        allNodes = []
        if self.head == None:
            return 0
        else:
            temp = self.head
            while temp.next:
                allNodes.append(temp.data)
                temp = temp.next
            return allNodes



class Graph_UUU():
    numNodes = 0
    adjacentList = {}

    def addVertex(self, node):
        if node in self.adjacentList:
            self.adjacentList[node] = linkedList(node)
        else:
            self.numNodes = self.numNodes + 1
        return self.adjacentList[node]

    def addEdge(self,node1,node2):
        try:
            self.adjacentList[node1].addNode(node2)
            self.adjacentList[node2].append(node2)
        except:
            print("One of the nodes does not exist please only make connections between created nodes")

        return self.adjacentList

    def makeConections(self):
        for key in self.adjacentList.keys():
            all_Nodes = self.adjacentList[key].getAll()
            print(f"{key} --> {all_Nodes}")
