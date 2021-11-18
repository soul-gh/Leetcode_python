#山峰数组（山脉数组） 

class Solution:
    def peakIndexInMountainArray(arr) -> int:
        left,right = 1,len(arr)-2
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
print(Solution.peakIndexInMountainArray(arr))
