
def bubbleSort(arr):
    changes = False
    not_sorted = True
    while not_sorted:
        for index,x in enumerate(arr[0:len(arr)-1]):
            if x > arr[index+1]:
                arr[index] = arr[index+1]
                arr[index + 1] = x
                changes = True
        if not changes:
            not_sorted = False
        changes = False
    return arr