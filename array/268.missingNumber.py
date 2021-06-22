#哈希表
class Solution:
    def missingNumber(nums):
        N = len(nums)
        set_nums = [0]*(N+1)
        for i in range(N):
            if set_nums[nums[i]] == 0:
                set_nums[nums[i]] = 1
        for j in range(N+1):
            if set_nums[j] == 0:
                return j
nums = [3,0,1]
print(Solution.missingNumber(nums))

#先排序，再找相邻差2的数
class Solution1:
    def missingNumber(nums):
        N = len(nums)
        nums.sort()
        if nums[0] != 0:
            return 0
        if nums[-1] != N:
            return N
        for i in range(1,N):
            if nums[i] - nums[i-1] == 2:
                return  i
nums = [3,0,1]
print(Solution1.missingNumber(nums))