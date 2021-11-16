#给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 
#请你统计并返回 grid 中 负数 的数目。

#全部遍历
class Solution:
    def countNegatives(grid) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    res += 1
        return res
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(Solution.countNegatives(grid))

#从右上角到左下角
class Solution1:
    def countNegatives(grid) -> int:
        i,j,res = 0,len(grid[0]) - 1,0
        while i < len(grid) and j >= 0:
            if grid[i][j] < 0:
                res += len(grid) - i
                j -= 1
            else:
                i += 1
        return res
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(Solution1.countNegatives(grid))