#输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

#暴力
class Solution:
    def twoSum(nums, target: int):
        res = []
        for i in nums:
            tmp = target - i
            if tmp in nums:
                res.append(i)
                res.append(tmp)
                return res
nums = [2,7,11,15]
print(Solution.twoSum(nums,9))

#双指针
class Solution1:
    def twoSum(nums, target: int):
        res = []
        i,j = 0,len(nums)-1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                res.append(nums[i])
                res.append(nums[j])
                return res
        return []
nums = [2,7,11,15]
print(Solution1.twoSum(nums,9))

#哈希表
class Solution2:
    def twoSum(nums, target: int) :
        dic = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if nums[i] not in dic:
                dic[tmp] = nums[i]
            else:
                return [dic[nums[i]],nums[i]]
        return[]
nums = [2,7,11,15]
print(Solution2.twoSum(nums,9))