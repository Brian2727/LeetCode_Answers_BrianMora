from DataStructures.BinarySearchTree import BinarySearchTree
from Strings.reverse import reverse


mytree = BinarySearchTree()
mytree.insert(20)
mytree.insert(7)
mytree.insert(80)
mytree.insert(7)
mytree.insert(40)
mytree.insert(20)

print(mytree.root)
print(mytree.delete(80))
print(mytree.root)
print(mytree.delete(20))
print(mytree.delete(20))
print(mytree.delete(20))
print(mytree.root)