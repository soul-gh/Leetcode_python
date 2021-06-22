#双指针
class Solution:
    def moveZeroes(nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                res = j
                break
            if i == len(nums)-1:
                return
        for i in range(res+1,len(nums)):
            if nums[i] != 0:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                j += 1
nums = [0,1,0,3,12]
Solution.moveZeroes(nums)
print(nums)
