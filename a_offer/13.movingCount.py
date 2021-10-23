#地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
# 一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
# 也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
# 因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

#DFS
#首先创建visited数组用于记录已被访问的节点，已被访问设为1，还没被访问设为0，另外不能被访问的位置也设为1
#因为从(0, 0)位置开始遍历数组，因此只会从往右和往下两个方向走
#递归的返回值为该机器人能够到达的格子数量，每次递归1个格子，因此每次返回值 + 1：1 + dfs(x + 1, y) + dfs(x, y + 1)
#递归中，如果当前位置(x, y)不在方格范围内或者已被访问过，返回0
class Solution:
    def movingCount(m: int, n: int, k: int) -> int:
        def sums(x):  #位数和
            sum = 0
            while x != 0:
                sum += x % 10
                x = x//10
            return sum

        visited = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range( n):
                if sums(i) + sums(j) <= k:
                    visited[i][j] = 0
        
        def dfs(row,col):
            if row < 0 or row >= m or col < 0 or col >= n or visited[row][col]:
                return 0
            visited[row][col] = 1
            return 1 + dfs(row+1,col) + dfs(row,col+1)
        return dfs(0,0)

print(Solution.movingCount(3,2,17))