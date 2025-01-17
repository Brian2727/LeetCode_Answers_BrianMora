from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        totalBits = 0
        arrSize = len(derived)
        if arrSize == 1:
            if derived[0] == 0:
                return True
            else:
                return False

        for b in derived:
            totalBits += b

        if arrSize % 2 >= 1:
            if totalBits % 2 == 0:
                return True
        elif arrSize % 2 == 0 and (totalBits % 2 == 0 or totalBits == 0):
            return True

        return False
