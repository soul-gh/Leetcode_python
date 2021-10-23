#输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

#普通
class Solution:
    def findContinuousSequence(target: int):
        res = []
        for i in range(1,(target//2)+1):
            tmp,sum1 = [],0
            j = i
            while sum1 < target:
                tmp.append(j)
                sum1 += j
                j += 1
                if sum1 == target:
                    res.append(tmp)
                elif sum1 > target:
                    break
                else:
                    continue
        return res
print(Solution.findContinuousSequence(9))

#滑动窗口
class Solution1:
    def findContinuousSequence(target: int):
        i,j,s,res = 1,2,3,[]
        while i < j:
            if s == target:
                res.append(list(range(i,j+1)))
                s -= i
                i += 1
            elif s > target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res
print(Solution1.findContinuousSequence(9))