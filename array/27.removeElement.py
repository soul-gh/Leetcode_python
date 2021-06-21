#快慢指针
class Solution:
    def removeElement(nums, val):
        left = 0
        for right in nums:
            if right != val:
                nums[left]=right
                left += 1
        return left
nums = [3,2,2,3]
val = 3
print(Solution.removeElement(nums,val))
print(nums[:2])
print("\n")

#错误！ 
#for循环在一开始就确定了遍历顺序，所以在for循环中使用remove，会改变原本的数组顺序
class Solution1:
    def removeElement(nums, val):
        i = 0
        for num in nums:
            if num == val:
                nums.remove(val)
            else:
                i += 1
        return i
nums = [3,2,2,3]
val = 3
print(Solution1.removeElement(nums,val))
print(nums)