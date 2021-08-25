#

#笨
class Solution:
    def missingNumber(nums) -> int:
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            if nums[0] == 1:
                return 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] != 1:
                return nums[i]-1
        if nums[0] != 0:
            return 0
        else:
            return nums[i]+1

nums = [0,1,3]
print(Solution.missingNumber(nums))

#二分搜索
class Solution1:
    def missingNumber(nums) -> int:
        i,j = 0,len(nums) - 1
        while i <= j:
            m = (i + j)//2
            if nums[m] == m:
                i = m + 1
            else :
                j = m - 1
        return i
nums = [0,1,3]
print(Solution1.missingNumber(nums))