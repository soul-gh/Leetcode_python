#找出数组中重复的数字。
#hash
class Solution:
    def findRepeatNumber(nums):
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                return nums[i]
nums = [2, 3, 1, 0, 2, 5, 3]
print(Solution.findRepeatNumber(nums))

#鸽巢原理，原地hash
class Solution:
    def findRepeatNumber(nums):
        n = len(nums)
        for i in range(n):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]] = nums[i]
                nums[i] = nums[nums[i]] 
