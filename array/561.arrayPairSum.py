#列表分为两两一组，两数中较小的一个的和最大为
#sort
class Solution:
    def arrayPairSum(nums):
        nums.sort()
        sum = 0
        for i in range(1,len(nums),2):
           sum += min(nums[i],nums[i-1])
        return sum
nums = [1,4,3,2]
print(Solution.arrayPairSum(nums))

#切片
class Solution1:
    def arrayPairSum(nums):
        nums.sort()
        return sum(nums[::2])
nums = [1,4,3,2]
print(Solution1.arrayPairSum(nums))