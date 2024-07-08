def findFactorialRecursive(number):
    if number == 1:
        return number
    return number * findFactorialRecursive(number-1)

def fibonacciSequenceRecursive(n): #n means index of the fibonachi sequence.
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacciSequenceRecursive(n-1) + fibonacciSequenceRecursive(n-2)