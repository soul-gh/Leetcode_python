#请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

#递归DFS
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(root: TreeNode) -> bool:
        def dfs(L,R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return dfs(L.left,R.right) and dfs(L.right,R.left)
        return dfs(root.left,root.right) if root else True
tree = [1,2,2,3,4,4,3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3) 
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(Solution.isSymmetric(root))

