#符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：
#arr.length >= 3
#存在 i（0 < i < arr.length - 1）使得：
#arr[0] < arr[1] < ... arr[i-1] < arr[i]
#arr[i] > arr[i+1] > ... > arr[arr.length - 1]
#给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i ，即山峰顶部。

#遍历
class Solution:
    def peakIndexInMountainArray(arr) -> int:
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                return i-1
arr = [0,1,0]
print(Solution.peakIndexInMountainArray(arr))

#二分搜索
class Solution1:
    def peakIndexInMountainArray(arr) -> int:
        n = len(arr)
        left,right = 1,n-2
        while left < right:
            mid = (left + right)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid-1]:
                left = mid + 1
            else:
                right = mid - 1
        return left
arr = [0,1,0]
print(Solution1.peakIndexInMountainArray(arr))