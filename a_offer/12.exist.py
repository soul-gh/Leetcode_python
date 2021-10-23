#给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#矩阵搜索问题，可使用 深度优先搜索（DFS）+ 剪枝      递归
class Solution:
    def exist(board, word):
        def dfs(row,col,k):
            if not 0 <= row < len(board) or not 0 <= col < len(board[0]) or word[k] != board[row][col]:
                return False
            if k == len(word) - 1:
                return True        #前两个if是递归返回条件
            board[row][col] = ' '   #选取的位置置为空，防止下一步递归重复访问
            res = dfs(row,col+1,k+1) or dfs(row,col-1,k+1) or dfs(row+1,col,k+1) or dfs(row-1,col,k+1)
            board[row][col] = word[k]   #board复原
            return res
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row,col,0):
                    return True
        return False
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(Solution.exist(board,word))