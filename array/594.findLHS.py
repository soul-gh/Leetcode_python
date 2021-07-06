#最长和谐子序列 数组里元素的最大值和最小值之间的差别正好是 1 。
class Solution:
    def findLHS(nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        res = 0
        for i in dic:
            if i+1 in dic:
                res = max(res,dic[i+1]+dic[i])
        return res
nums = [1,3,2,2,5,2,3,7]
print(Solution.findLHS(nums))