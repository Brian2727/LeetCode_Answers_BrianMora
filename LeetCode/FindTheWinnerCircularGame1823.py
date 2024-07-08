def findTheWinner(n, k):
    class Node:
        next = None

        def __init__(self, value):
            self.value = value

    class circularList:
        current_node = None
        size = 0

        def addNode(self, value):
            new_node = Node(value)
            if self.current_node is None:
                self.current_node = new_node
                self.current_node.next = self.current_node
                self.size += 1
            else:
                temp = self.current_node
                while temp.next != self.current_node:
                    temp = temp.next
                temp.next = new_node
                temp.next.next = self.current_node
                self.size += 1

        def removeValue(self, value):
            prev = self.current_node
            temp = self.current_node.next
            if self.current_node.value == value:
                while temp.next != self.current_node:
                    temp = temp.next
                self.current_node = self.current_node.next
                temp.next = self.current_node
                self.size -= 1
                return value
            else:
                if temp.value == value:
                    prev.next = temp.next
                    self.size -= 1
                    return value
                while temp.next != self.current_node:
                    if temp.value == value:
                        prev.next = temp.next
                        self.size -= 1
                        return value
                    temp = temp.next
                    prev = prev.next
            return "notFound"

    friend_circle = circularList()
    for f in range(n):
        friend_circle.addNode(f+1)

    while friend_circle.size > 1:

        for f in range(k-1):
            friend_circle.current_node = friend_circle.current_node.next

        print(f'removing {friend_circle.current_node.value}')
        friend_circle.removeValue(friend_circle.current_node.value)

    return friend_circle.current_node.value



