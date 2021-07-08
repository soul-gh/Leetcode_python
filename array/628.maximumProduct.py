#在数组中找出由三个数组成的最大乘积，并输出这个乘积。
#**********找到最大的三个数和最小的两个数************
#排序
class Solution:
    def maximumProduct(nums):
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
nums = [1,2,3,4]
print(Solution.maximumProduct(nums))

#不排序
class Solution1:
    def maximumProduct(nums):
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for num in nums:
            if num < min1:
                min2 = min1  #原来的最小变成第二小
                min1 = num   #更新最小值
            elif num < min2:
                min2 = num  
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
        return max(max1*max2*max3,min1*min2*max1)
nums = [1,2,3,4]
print(Solution1.maximumProduct(nums))