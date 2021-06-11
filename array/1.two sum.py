#方法1 ： 暴力
class Solution:
    #def __init__(self,nums,target):
     #   self.nums = nums
      #  self.target = target
    def twoSum(nums, target):
        List1 = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    List1.append(int(i))
                    List1.append(int(j))
                    return List1
        return List1
nums = [2,7,11,15]
target = 9
#list1 = Solution(nums,target)
list2 = Solution.twoSum(nums,target)
print(list2)

#方法2 ： 使用in的暴力
class Solution:
    def twoSum(nums, target):
        for i in range(len(nums)-1):
            base = nums[i]
            other = target - base
            if other in nums[i+1:len(nums)]:
                return [i,nums.index(other,i+1)]
nums = [2,7,11,15]
target = 9
print(Solution.twoSum(nums,target))

#方法3 ： 哈希表
class Solution:
    def twoSum(nums, target):
        tmp = {}
        for k, v in enumerate(nums):        #枚举,key里放值，value里放索引
            if target - v in tmp:
                return [tmp[target - v],k]
            tmp[v] = k
nums = [2,7,11,15]
target = 9
print(Solution.twoSum(nums,target))
print(list(enumerate(nums)))