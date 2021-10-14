#给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。
#返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：
#如果 S[i] == "I"，那么 A[i] < A[i+1]
#如果 S[i] == "D"，那么 A[i] > A[i+1]

#‘I’ 取最小   ‘D 取最大’
class Solution:
    def diStringMatch(s: str) :
        table = [num for num in range(len(s)+1)]
        res = []
        for mark in s:
            if mark == "I":
                res.append(table.pop(0))
            else:
                res.append(table.pop(-1))
        res.append(table.pop(0))
        return res
s = "IDID"
print(Solution.diStringMatch(s))