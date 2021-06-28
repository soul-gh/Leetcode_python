#找到数组中消失的数字

# in判断
class Solution:
    def findDisappearedNumbers(nums):
        res = []
        tmp = set(nums)
        for i in range(1,len(nums)+1):
            if i not in tmp:
                res.append(i)
        return res
nums = [4,3,2,7,8,2,3,1]
print(Solution.findDisappearedNumbers(nums))


