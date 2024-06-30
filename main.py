from DataStructures.BinarySearchTree import BinarySearchTree
from DataStructures.Graphs import Graph_UUU
from Strings.reverse import reverse


my_graph = Graph_UUU()

my_graph.addVertex(2)
my_graph.addVertex(1)
my_graph.addVertex(3)
my_graph.addVertex(5)
my_graph.addVertex(8)
my_graph.addEdge(1,2)
my_graph.addEdge(1,8)
my_graph.addEdge(2,8)
my_graph.addEdge(5,2)
my_graph.addEdge(5,8)
my_graph.addEdge(1,5)

my_graph.makeConections()




