class MedianFinder:
    #I'm going ot use a doubly lined list since inserts on linked list are O(1) and is easy to add values in the middle.
    #Calculating the media should be O(n/2) since we only have to loop to the middle of the list.
    class Node:
        def __init__(self,val=None):
            self.val = val
            self.prev = None
            self.next = None


    def __init__(self):
        self.head = self.Node()
        self.size = 0

    def addNum(self, num):
        if self.size == 0:
            self.head.val = num
            self.size += 1
            return
        curr_size = self.size
        temp = self.head
        while temp.next is not None:

            if temp.val >= num:
                prev = temp.prev
                temp.prev = self.Node(num)
                temp.prev.next = temp
                self.size += 1
                if prev:
                    prev.next = temp.prev
                else:
                    self.head = temp.prev
                break
            else:
                temp = temp.next

        if curr_size == self.size:
            self.size += 1
            if num > temp.val:
                temp.next = self.Node(num)
                temp.next.prev = temp
            else:
                temp.prev = self.Node(num)
                self.head = temp.prev
                self.head.next = temp

    def findMedian(self):
        pass

    def __str__(self):
        answ = ('')
        temp = self.head
        while temp.next is not None:
            answ =  answ + " - " + str(temp.val)
            temp = temp.next

        return answ + " - " + str(temp.val)