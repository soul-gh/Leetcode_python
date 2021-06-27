#遍历一次，更新第一二三大的数字
class Solution:
    def thirdMax(nums):
        tmps = list(set(nums))
        if len(tmps) < 3:
            return max(tmps)
        f = s = t = float('-inf')
        for tmp in tmps:
            if tmp > f:
                t = s
                s = f
                f = tmp
            elif tmp > s:
                t = s
                s = tmp
            elif tmp > t:
                t = tmp
        return t
nums = [-1,2,3]
print(Solution.thirdMax(nums))