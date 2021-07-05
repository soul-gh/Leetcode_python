#矩阵重新造型
#创建指定大小的二维数组*  一维数据要[None]*r，然后再for循环定义二维
class Solution:
    def matrixReshape(mat, r, c):
        R = len(mat)
        C = len(mat[0])
        if r * c != R*C:
            return mat
        else:
            tmp = []
            res = [None]*r
            for i in range(len(res)):
                res[i] = [0] * c
            for i in range(R):
                for j in range(C):
                    tmp.append(mat[i][j])
            k = 0
            for i in range(len(res)):
                for j in range(len(res[i])):
                    res[i][j] = tmp[k] 
                    k += 1
            return res
nums = [[1,2],[3,4]]
r = 1
c = 4
print(Solution.matrixReshape(nums,r,c))

#直接利用索引赋值
class Solution1:
    def matrixReshape(mat, r, c):
        R = len(mat)
        C = len(mat[0])
        if r * c != R*C:
            return mat
        else:
            tmp = []
            res = [None]*r
            for i in range(len(res)):
                res[i] = [0] * c
            for i in range(R*C):
                res[i//c][i%c] = mat[i//C][i%C]
            return res
nums = [[1,2],[3,4]]
r = 1
c = 4
print(Solution1.matrixReshape(nums,r,c))