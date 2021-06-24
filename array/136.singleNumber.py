#哈希表
class Solution:
    def singleNumber(nums):
        set = {}
        for i in range(len(nums)):
            if nums[i] not in set:
                set[nums[i]] = 1
            else:
                set[nums[i]] = 0
        for key,value in set.items():
            if value == 1:
                return key
nums = [2,2,1]
print(Solution.singleNumber(nums))

#位异或
class Solution1:
    def singleNumber(nums):
        tmp = nums[0]
        for i in range(1,len(nums)):
            tmp ^= nums[i] 
        return tmp
nums1 = [2,2,1]
print(Solution1.singleNumber(nums1))
