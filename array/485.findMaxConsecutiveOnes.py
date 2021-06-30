#找出数组中最多的连续1的个数
class Solution:
    def findMaxConsecutiveOnes(nums):
        cnt = Max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                if cnt > Max:
                    Max = cnt
            else:
                if cnt > Max:
                    Max = cnt
                cnt = 0
        return Max
nums = [1,1,0,1,1,1]
print(Solution.findMaxConsecutiveOnes(nums))