#前缀和
class NumArray:
    def __init__(self, nums):
        N = len(nums)
        self.presum = [0]*(N+1)
        for i in range(N):
            self.presum[i+1] = self.presum[i] + nums[i]
    def sumRange(self, left , right):
        return self.presum[right+1] - self.presum[left]

nums = [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]