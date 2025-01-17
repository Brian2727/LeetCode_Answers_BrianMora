from random import random


class RandomizedSet:

    def __init__(self):
        self.randomArray = []
        self.randomSet = {}
        self.numElements = 0

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        else:
            self.randomArray.append(val)
            self.randomSet[val] = self.numElements
            self.numElements += 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            item_to_del_index = self.randomSet[val]
            last_item_value = self.randomArray[-1]
            self.randomSet[last_item_value] = item_to_del_index
            self.randomArray[item_to_del_index] = last_item_value
            del self.randomSet[val]
            self.randomArray.pop()
            self.numElements -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:

        return random.choice(self.randomArray)