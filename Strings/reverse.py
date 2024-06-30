# This is for creating a couple of functions to reverse strings in different ways and different time complexities.

#time complexity O(n)
def reverse(str):
    reversed = ''
    for i in range(len(str)):
        reversed = reversed+str[len(str)-i-1]
    return reversed
