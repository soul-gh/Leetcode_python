#超时
class Solution:
    def twoSum(numbers, target):
        res = [0,0]
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    res[0] = i + 1
                    res[1] = j + 1
                    return res
numbers = [2,3,5,6,7]
target = 11
print(Solution.twoSum(numbers,target))

#双指针
class Solution1:
    def twoSum(numbers, target):
        N = len(numbers)
        left,right = 0,N-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left] + numbers[right] >target:
                right -= 1
            else:
                left += 1
numbers = [2,3,5,6,7]
target = 11
print(Solution1.twoSum(numbers,target))