#Best Solution siuuuuuu

def luckyNumbers(matrix):
        # row mins
        rmin = [min(x) for x in matrix]

        # col maxs
        cmax = [max(x) for x in zip(*matrix)]

        return list(set(rmin) & set(cmax))


#My ugly Solution
def luckyNumbersBrian(matrix):
    biggestInRow = True
    luckyNumbers = []
    for row in matrix:
        smallestInRow = row[0]
        smallestIndex = 0
        for index, x in enumerate(row):

            if smallestInRow > x:
                smallestInRow = x
                smallestIndex = index

        for index, col in enumerate(matrix):
            print(f"Comparing col {col[smallestIndex]} > {smallestInRow}")
            if col[smallestIndex] > smallestInRow:
                biggestInRow = False
                break

        if biggestInRow:
            luckyNumbers.append(smallestInRow)
        else:
            biggestInRow = True

    return luckyNumbers