def minPathSum(grid):
    lowest_by_level = {}
    def helper(x,y,sum,level):
        if x >= len(grid[0])-1 and y >= len(grid)-1:
            sum += grid[y][x]
            return sum
        if x >= len(grid[0]) - 1:
            sum += grid[y][x]
            if level in lowest_by_level:
                if sum > lowest_by_level[level]:
                    return 10000
                else:
                    lowest_by_level[level] = sum
                    return helper(x, y + 1, sum,level+1)
            else:
                lowest_by_level[level] = sum
                return helper(x, y + 1, sum, level + 1)
        elif y >= len(grid) - 1:
            if level in lowest_by_level:
                if sum > lowest_by_level[level]:
                    return 10000
                else:
                    lowest_by_level[level] = sum
                    return helper(x + 1, y, sum,level+1)
            else:
                lowest_by_level[level] = sum
                return helper(x + 1, y, sum,level+1)
        else:
            sum += grid[y][x]
            left_path = helper(x+1,y,sum,level+1)
            down_path = helper(x,y+1,sum,level+1)
            if left_path > down_path:
                return down_path
            else:
                return left_path
    return helper(0,0,0,0)