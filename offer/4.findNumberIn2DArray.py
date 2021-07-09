#在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。查找元素target
#暴力
class Solution:
    def findNumberIn2DArray(matrix, target):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    continue
        return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(Solution.findNumberIn2DArray(matrix,target))

#将二维数组看成二叉搜索树
class Solution1:
    def findNumberIn2DArray(matrix, target):
        i = len(matrix)-1
        j = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False 
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(Solution1.findNumberIn2DArray(matrix,target))