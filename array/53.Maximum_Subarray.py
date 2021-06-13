class Solution:
    def maxSubArray(nums):
        if len(nums) == 0:
            return false
        max_sum = cur_sum = nums[0]
        for i in range(1,len(nums)):
            cur_sum = max(nums[i],nums[i]+cur_sum)
            max_sum = max(cur_sum,max_sum)
        return max_sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution.maxSubArray(nums))

class Solution:
    def maxSubArray(nums):
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution.maxSubArray(nums))