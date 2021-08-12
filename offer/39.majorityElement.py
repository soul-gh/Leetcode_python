#过半元素

#摩尔投票
class Solution:
    def majorityElement(nums) -> int:
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                target = nums[i]
                cnt += 1
            elif nums[i] == target:
                cnt += 1
            else:
                cnt -= 1
        return target
nums = [1,2,3,2,2,2,5,4,2]
print(Solution.majorityElement(nums))