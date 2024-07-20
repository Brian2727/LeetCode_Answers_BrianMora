from Algorithms.bubble_sort import bubbleSort
from Algorithms.merge_sort import mergeSort
from Algorithms.recursion import findFactorialRecursive, fibonacciSequenceRecursive
from Algorithms.selection_sort import selectionSort
from DataStructures.BinarySearchTree import BinarySearchTree
from DataStructures.GraphArrayConection import Graph
from LeetCode.FindTheWinnerCircularGame1823 import findTheWinner
from LeetCode.GenerateParentheses22 import GenerateParentheses
from LeetCode.MaxPointFromRemovingStrings import maximumGain, maximumGain2
from LeetCode.MinimumPathSum64 import minPathSum
from LeetCode.Pow import Solution
from LeetCode.rightSideViewOfTree17 import ViewFromRigthSide
from Strings.reverse import reverse

arr = [2,1,8,6,2,4,7,8,6]
grid = [[1,3,1,5,3],[1,5,1,5,2],[4,2,1,5,2]]
tree_initializer = [3,1,2,5,4,5,6,7]
tree = BinarySearchTree()
myGraph = Graph()

<<<<<<< Updated upstream
for x in tree_initializer:
    tree.insert(x)
print(tree)

right_side_view = ViewFromRigthSide(tree)
for x in range(8):
    myGraph.add_node(x)

myGraph.add_vertex(0,7)
myGraph.add_vertex(1,7)
myGraph.add_vertex(3,2)
myGraph.add_vertex(1,2)
myGraph.add_vertex(5,3)
myGraph.add_vertex(6,5)
myGraph.add_vertex(4,1)

#print(myGraph)
#print(myGraph.bfs(1,4))
s = "cdbcbbaaabab"
print(maximumGain2(s,4,5))
=======
>>>>>>> Stashed changes





