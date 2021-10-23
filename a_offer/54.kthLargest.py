#给定一棵二叉搜索树，请找出其中第k大的节点。

#DFS 右中左 ，从大到小
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root:
                return 
            dfs(root.right)
            Solution.k -= 1
            if Solution.k == 0:
                Solution.res = root.val
            dfs(root.left)
        Solution.k = k
        dfs(root)
        return Solution.res

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

print(Solution.kthLargest(root,1))