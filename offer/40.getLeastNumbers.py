#输入整数数组 arr ，找出其中最小的 k 个数.

#arr.sort()
class Solution:
    def getLeastNumbers(arr, k):
        arr.sort()
        res = []
        for i in range(k):
            res.append(arr[i])
        return res
arr = [3,2,1]
k = 2
print(Solution.getLeastNumbers(arr,k))

