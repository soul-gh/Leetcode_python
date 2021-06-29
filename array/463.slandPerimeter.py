#岛屿周长
#一个方块周长为4，两个为6....规律为4+（n+1）*2
#但是如果四个方块组成一个大方块周长就会减少2
class Solution:
    def islandPerimeter(grid):
        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    n += 1
                    if i != len(grid)-1 and j != len(grid[i])-1:
                        if grid[i][j+1] == grid[i+1][j] == grid[i+1][j+1] == 1:
                            n -= 1
        return 4+(n-1)*2
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(Solution.islandPerimeter(grid))