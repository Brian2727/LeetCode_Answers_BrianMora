def threeSum(self, nums):
    size = len(nums)
    ans = []
    ans_dic = {}
    numbers = {}
    for index_x, x in enumerate(nums):
        index_y = index_x + 1
        for i, y in enumerate(nums[index_y:size]):
            for z in nums[index_x + 2 + i:size]:
                if x + y + z == 0:
                    s = [x, y, z]
                    s.sort()
                    print(s)
                    if f"{s[0]}{s[1]}{s[2]}" in ans_dic:
                        continue
                    else:
                        ans_dic[f"{s[0]}{s[1]}{s[2]}"] = True
                        ans.append([x, y, z])
    return ans
