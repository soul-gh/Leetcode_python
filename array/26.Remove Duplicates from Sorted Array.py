#快慢指针
#left记录没有重复的。right遇到重复的直接跳过，遇到没有重复的放到left+1的位置，返回的left+1为所有不重复的数字
#考点：返回原数组，不能使用新数组
class Solution:
    def removeDuplicates(nums):
        left = 0
        N = len(nums)
        for right in range(1,N):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left+1
nums = [1,1,2,2,3]
nums = [2,3,4,5,5,6,7,7]
print(Solution.removeDuplicates(nums))
print(nums[:6])