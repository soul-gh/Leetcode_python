#超时
class Solution:
    def containsDuplicate(nums):
        for i in nums:
            cnt = 0
            for j in nums:
                if i == j:
                    cnt +=1
                if cnt == 2:
                    return True
        return False
nums = [2,1,3,4,5,6,1]
print(Solution.containsDuplicate(nums))

#排序后检查相邻数字是否相同
class Solution1:
    def containsDuplicate(nums):
        nums.sort()
        for i in range(len(nums)-1): 
            if nums[i] == nums[i+1]:
                return True
        return False
nums = [2,1,3,4,5,6,1]
print(Solution1.containsDuplicate(nums))

#set去重
class Solution2:
    def containsDuplicate(nums):
        return len(set(nums)) != len(nums)
nums = [2,1,3,4,5,6,1]
print(Solution2.containsDuplicate(nums))

#哈希表
class Solution3:
    def containsDuplicate(nums):
        set_num = {}
        for i in nums:
            if i not in set_num:
                set_num[i] = 1
            else:
                return True
        return False
nums = [2,1,3,4,5,6,1]
print(Solution3.containsDuplicate(nums))
