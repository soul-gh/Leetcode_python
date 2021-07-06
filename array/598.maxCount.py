#给定一个初始元素全部为 0，大小为 m*n 的矩阵 M 以及在 M 上的一系列更新操作。返回矩阵中含有最大整数的元素个数。
#超时
class Solution:
    def maxCount(m,n,ops):
        M = [None] * m
        for i in range(m):
            M[i] = [0] * n
        for i in range(len(ops)):
            for j in range(ops[i][0]):
                for k in range(ops[i][1]):
                    M[j][k] += 1
        print(M)
        tmp = []
        for i in range(m):
            for j in range(n):
                tmp.append(M[i][j])
        max_num = max(tmp)
        res = 0
        for i in range(len(tmp)):
            if tmp[i] == max_num:
                res += 1
        return res
m = 3
n = 3
operations = [[2,2],[3,3]]
print(Solution.maxCount(m,n,operations))

#直接输出操作重叠部分的长乘宽
class Solution1:
    def maxCount(m,n,ops):
        col = []
        row = []
        if not ops:
            return m * n
        for op in ops:
            col.append(op[0])
            row.append(op[1])
        min_col = min(col)
        min_row = min(row)
        return min_col * min_row
m = 3
n = 3
operations = [[2,2],[3,3]]
print(Solution1.maxCount(m,n,operations))