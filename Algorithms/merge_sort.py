
def mergeSort(arr):
    if len(arr) == 1:
        return arr

    left = arr[0:int(len(arr)/2)]
    right = arr[int(len(arr)/2):len(arr)]

    return merge(mergeSort(left),mergeSort(right))

def merge(arr1,arr2):
    mergedArr = []
    counterLeft = 0
    counterRight = 0
    while counterLeft < len(arr1) or counterRight < len(arr2):
        if counterLeft >= len(arr1):
            mergedArr = mergedArr + arr2[counterRight:len(arr2)]
            counterRight = counterRight + len(arr2) - counterRight
        elif counterRight >= len(arr2):
            mergedArr = mergedArr + arr1[counterLeft:len(arr1)]
            counterLeft = counterLeft + len(arr1)-counterLeft
        elif arr1[counterLeft] < arr2[counterRight]:
            mergedArr.append(arr1[counterLeft])
            counterLeft = counterLeft + 1
        elif arr1[counterLeft] > arr2[counterRight]:
            mergedArr.append(arr2[counterRight])
            counterRight =  counterRight + 1
        elif arr1[counterLeft] == arr2[counterRight]:
            mergedArr.append(arr2[counterRight])
            counterRight = counterRight + 1
            mergedArr.append(arr1[counterLeft])
            counterLeft = counterLeft + 1
    return mergedArr