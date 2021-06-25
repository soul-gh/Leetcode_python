#双指针
import math
class Solution:
    def summaryRanges(nums):
        res = []
        if len(nums) == 1:
            res = [str(nums[0])]
            return res
        left = 0
        nums.append(math.inf)#多放一位，保证最后一位的输出
        for right in range(1,len(nums)):
            if right-1 == left and nums[right] - nums[right-1] != 1:
                res.append(str(nums[left]))
                left = right
            elif right-1 != left and nums[right] - nums[right-1] != 1:
                res.append(str(nums[left]) + '->' + str(nums[right-1]))
                left = right
        return res
nums = [0,1,2,4,5,7]
print(Solution.summaryRanges(nums))