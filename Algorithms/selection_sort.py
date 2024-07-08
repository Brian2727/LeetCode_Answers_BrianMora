def selectionSort(arr):
    for index_x,x in enumerate(arr[0:len(arr)-1]):
        index_y = index_x
        while index_y < len(arr):
            print(f"comparing ({arr[index_x]} < {arr[index_y]})")
            if arr[index_x] > arr[index_y]:
                temp = arr[index_y]
                arr[index_y] = arr[index_x]
                arr[index_x] = temp
            index_y = index_y+1
    return arr