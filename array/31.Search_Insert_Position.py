#暴力法
class Solution:
    def searchInsert(nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
nums = [1,3,5,6]
target = 7
print(Solution.searchInsert(nums,target))

#二叉树
class Solution:
    def searchInsert(nums, target):
        left,right = 0,len(nums)
        mid = 0
        while left < right:
            mid = (left + right)//2    #/表示浮点除法 ，//表示除法
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid 
        return left
nums = [1,3,5,6]
target = 7
print(Solution.searchInsert(nums,target))
