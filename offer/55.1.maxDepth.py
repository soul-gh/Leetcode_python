class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(root: TreeNode) -> int:
        if not root:
            return 0
        left = Solution.maxDepth(root.left)
        right = Solution.maxDepth(root.right)
        return max(left,right)+1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution.maxDepth(root))