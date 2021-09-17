#给你一个字符串 s 和一个 长度相同 的整数数组 indices 。
#请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。
#返回重新排列后的字符串。

class Solution:
    def restoreString(s: str, indices) -> str:
        res = [0] * len(indices)
        j = 0
        for i in indices:
            res[i] = s[j]
            j += 1
        return ''.join(res)
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(Solution.restoreString(s,indices))