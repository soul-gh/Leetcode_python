#哈希表    abs():绝对值函数
class Solution:
    def containsNearbyDuplicate(nums, k):
        set_num = {}
        for i in range(len(nums)):
            if nums[i] not in set_num:
                set_num[nums[i]] = i
            else:
                if abs(set_num[nums[i]]-i) <= k:
                    return True
                else:
                    set_num[nums[i]] = i        
        return False
nums = [1,2,3,1]
k = 3
print(Solution.containsNearbyDuplicate(nums,k))