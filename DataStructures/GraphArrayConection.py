
#this is a bidirectional graph meaning that if node a is connected to node b you can go from b to a and from a to b
class Graph:
    adjacentList = {}
    num_nodes = 0

    def add_node(self,node):
        if node in self.adjacentList:
            self.adjacentList[node] = set()
        else:
            self.adjacentList[node] = set()
            self.num_nodes += 1

    def add_vertex(self,node1,node2):
        if node1 in self.adjacentList and node2 in self.adjacentList:
            self.adjacentList[node1].add(node2)
            self.adjacentList[node2].add(node1)
        else:
            return "One of the nodes is missing cannot make a connection between missing nodes"

    def bfs(self,node1,node2):
        queqe = []
        arr_dis = [10000 for x in range(self.num_nodes)]
        current_node = node1
        arr_dis[node1] = 0
        queqe.append(current_node)
        while arr_dis[node2] == 10000 and len(queqe) > 0:
            current_node = queqe.pop()
            for c in self.adjacentList[current_node]:
                queqe.append(c)
                arr_dis[c] = arr_dis[current_node]+1
        print(arr_dis)
        return arr_dis[node2]

    def __str__(self):
        conections_str = ""
        for key in self.adjacentList:
            conections_str += "("+ str(key) +")--"
            for connection in self.adjacentList[key]:
                conections_str += "-("+str(connection)+')-'
            conections_str += "\n"
        return conections_str



