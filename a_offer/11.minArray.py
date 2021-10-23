#把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

#python养人
class Solution:
    def minArray(numbers) -> int:
        return min(numbers)

nums = [3,4,5,1,2]
print(Solution.minArray(nums))

#从末尾向前寻找旋转点
class Solution1:
    def minArray(numbers) -> int:
        for i in range(len(numbers)-1,-1,-1):
            if numbers[i] < numbers[i-1]:
                return numbers[i]
        return numbers[0]

nums = [3,4,5,1,2]
print(Solution1.minArray(nums))

#二分查找
#判断对象全部是high
class Solution2:
    def minArray(numbers) -> int:
        low, high = 0,len(numbers)-1
        while(low < high):
            mid = (low + high)// 2
            if numbers[mid] < numbers[high]:#mid小于high，说明旋转点在mid左侧，并且可能是mid
                high = mid
            elif numbers[mid] > numbers[high]: #mid大于high，说明旋转点在mid右侧
                low = mid + 1
            else:          
                             #第三种情况是high == mid,由于重复元素的存在，不能确定mid究竟在最小值的左侧还是右侧.
                            #因此我们不能莽撞地忽略某一部分的元素。我们唯一可以知道的是，由于它们的值相同.
                            #所以无论high是不是最小值，都有一个它的「替代品」mid,因此我们可以忽略二分查找区间的右端点。
                high -= 1
        return numbers[low]
nums = [2,2,2,0,1]  
print(Solution2.minArray(nums))