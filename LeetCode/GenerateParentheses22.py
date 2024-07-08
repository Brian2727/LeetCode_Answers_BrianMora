from rpds import List


class GenerateParentheses:

    def generateParenthesis(self, n: int):
        counter = 0
        list_of_combinations = []

        def addParenthesis(mainStr,openCount,closeCount):
            temp = mainStr
            if openCount > n and closeCount > n:
                list_of_combinations.append(mainStr)
                return
            print(f'o count{openCount} c count{closeCount}')
            if openCount > closeCount:
                mainStr += ')'
                addParenthesis(mainStr,openCount,closeCount+1)
            if openCount <= n:
                mainStr = temp
                mainStr += '('
                addParenthesis(mainStr,openCount+1,closeCount)
            return

        addParenthesis('',0,0)
        return list_of_combinations