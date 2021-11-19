#两个数对 (a, b) 和 (c, d) 之间的 乘积差 定义为 (a * b) - (c * d) 。
#例如，(5, 6) 和 (2, 7) 之间的乘积差是 (5 * 6) - (2 * 7) = 16 。
#给你一个整数数组 nums ，选出四个 不同的 下标 w、x、y 和 z ，使数对 (nums[w], nums[x]) 和 (nums[y], nums[z]) 之间的 乘积差 取到 最大值 。
#返回以这种方式取得的乘积差中的 最大值 。

class Solution:
    def maxProductDifference(nums) -> int:
        mx1,mx2 = max(nums[0],nums[1]),min(nums[0],nums[1])
        mn1,mn2 = min(nums[0],nums[1]),max(nums[0],nums[1])
        for i in range(2,len(nums)):
            if nums[i] > mx1:
                mx1,mx2 = nums[i],mx1
            elif nums[i] > mx2:
                mx2 = nums[i]
            if nums[i] < mn1:
                mn1,mn2 = nums[i],mn1
            elif nums[i] < mn2:
                mn2 = nums[i]
        return mx1*mx2 - mn1*mn2
nums = [5,6,2,7,4]
print(Solution.maxProductDifference(nums))