#统计一个数字在排序数组中出现的次数。

class Solution:
    def search(nums, target: int) -> int:
        cnt = 0
        for i in nums:
            if i == target:
                cnt += 1
        return cnt

#二分查找
class Solution1:
    def search(nums, target: int) -> int:
        def helper(target):
            i,j = 0,len(nums)-1
            while i < j:
                m = (i+j)//2
                if nums[m] <= target:
                    i = m + 1
                else:
                    j = m - 1
            return i
        return helper(target) - helper(target-1)
nums = [5,7,7,8,8,10]
print(Solution1.search(nums,8))
