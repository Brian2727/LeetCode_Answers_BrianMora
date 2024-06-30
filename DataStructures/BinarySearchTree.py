


class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
    def __str__(self):
        return f"[value:{self.value},left:{self.left},right:{self.right}]"

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self,value):
        if not self.root:
            self.root = Node(value)
            return self.root
        else:
            temp = self.root
            while True:
                if value > temp.value:
                    if not temp.right:
                        temp.right = Node(value)
                        return temp.right
                    else:
                        temp = temp.right
                else:
                    if not temp.left:
                        temp.left = Node(value)
                        return temp.left
                    else:
                        temp = temp.left

    def lookup(self,value):
        num_of_jumps = 0
        if value == self.root.value:
            return f'value found on {num_of_jumps}'
        else:
            temp = self.root
            while True:
                if temp.value == value:
                    return f'value found on {num_of_jumps}'
                elif value > temp.value:
                    temp = temp.right
                else:
                    temp = temp.left
                num_of_jumps = num_of_jumps+1

    def delete(self,value):
        num_of_jumps = 0
        move = ''
        if value == self.root.value:
            if self.root.right:
                temp_left = self.root.left
        else:
            temp = self.root
            prev = temp
            while True:
                try:
                    if temp.value == value:
                        if temp.right:
                            if move == 'R':
                                prev.right = temp.right
                            else:
                                prev.left = temp.right
                        elif temp.left:
                            if move == 'R':
                                prev.right = temp.left
                            else:
                                prev.left = temp.left
                        else:
                            if move == 'R':
                                prev.right = None
                            else:
                                prev.left = None
                        return f'value found on {num_of_jumps} and deleted'
                    elif value > temp.value:
                        move = 'R'
                        prev = temp
                        temp = temp.right
                    elif value < temp.value:
                        move = 'L'
                        prev = temp
                        temp = temp.left
                    else:
                        return f"Value Not Found Sorry"

                    num_of_jumps = num_of_jumps + 1




                except:
                    return f"Value Not Found Sorry"

    def remove(self,value):
        num_of_jumps = 0
        move = ''
        if value == self.root.value:
            if self.root.right:
                temp_left = self.root.left
        else:
            temp = self.root
            prev = temp
            while True:
                try:
                    if temp.value == value:
                        if temp.right:
                            if move == 'R':
                                prev.right = temp.right
                            else:
                                prev.left = temp.right
                        elif temp.left:
                            if move == 'R':
                                prev.right = temp.left
                            else:
                                prev.left = temp.left
                        else:
                            if move == 'R':
                                prev.right = None
                            else:
                                prev.left = None
                        return f'value found on {num_of_jumps} and deleted'
                    elif value > temp.value:
                        move = 'R'
                        prev = temp
                        temp = temp.right
                    elif value < temp.value:
                        move = 'L'
                        prev = temp
                        temp = temp.left
                    else:
                        return f"Value Not Found Sorry"

                    num_of_jumps = num_of_jumps + 1
                except:
                    return f"Value Not Found Sorry"