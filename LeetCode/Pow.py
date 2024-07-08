from _decimal import Decimal


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def powMem(x,n):
            if n == 0:
                return 1
            if x == 0 or x == 1:
                return float(x)
            if abs(n) <= 1:
                return x
            result = powMem(x * x,n//2.0)
            return result * x if n%2 > 0 else result
        result = float(powMem(x,float(n)))
        if n < 0:
            return float(1 / (result))
        else:
            return result
