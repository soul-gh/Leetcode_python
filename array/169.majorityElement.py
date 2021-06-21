#超时
class Solution:
    def majorityElement(nums):
        max_cnt = max_num = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
                max_num = nums[i]
        return max_num
nums = [1,1,1,1,1,5,5,5,5,5,5,5,5,5]
print(Solution.majorityElement(nums))

#摩尔投票
class Solution1:
    def majorityElement(nums):
        N = len(nums)
        cnt = 0
        target_num = nums[0]
        for num in nums:
            if num == target_num:
                cnt += 1
            elif num != target_num:
                cnt -= 1
            if cnt == -1:
                target_num = num
                cnt = 0
        return target_num
nums = [1,1,1,1,1,5,5,5,5,5,5,5,5,5]
print(Solution1.majorityElement(nums))