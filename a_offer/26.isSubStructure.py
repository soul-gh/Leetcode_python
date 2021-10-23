#输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构).B是A的子结构， 即 A中有出现和B相同的结构和节点值。
#DFS 递归
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(A: TreeNode, B: TreeNode) -> bool:
        if B == None or A == None:
            return False
        def dfs(A: TreeNode, B: TreeNode):
            if B == None:
                return True
            if A == None or B.val != A.val:
                return False
            if B.val == A.val:
                if dfs(A.left,B.left):
                    if dfs(A.right,B.right):
                        return True
        if dfs(A,B) or Solution.isSubStructure(A.left,B) or Solution.isSubStructure(A.right,B):
            return True
        return False

A = TreeNode(1)
A.left = TreeNode(2)
A.right = TreeNode(3)
A.left.left = TreeNode(4)
B = TreeNode(3)

print(Solution.isSubStructure(A,B))