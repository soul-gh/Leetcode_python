#输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
#数组拼接
class Solution:
    def exchange(nums):
        odd = []
        even = []
        for _ in nums:
            if _ % 2 == 1:
                odd.append(_)
            else:
                even.append(_)
        return odd+even
nums = [1,2,3,4]
print(Solution.exchange(nums))
#前后双指针
class Solution1:
    def exchange(nums):
        n = len(nums)
        i,j = 0,n-1
        while i <= j:
            if nums[i] % 2 == 0 and nums[j] % 2 == 1:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
            elif nums[i] % 2 == 1 and nums[j] % 2 == 1:
                i += 1
            elif nums[i] % 2 == 0 and nums[j] % 2 == 0:
                j -= 1
            else:
                i += 1
                j -= 1
        return nums
nums = [1,2,3,4]
print(Solution1.exchange(nums))

#快慢指针
class Solution2:
    def exchange(nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] % 2 == 1:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
        return nums 
nums = [1,2,3,4]
print(Solution2.exchange(nums))