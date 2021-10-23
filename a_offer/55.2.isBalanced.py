#输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中*任意节点*的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

#任意节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(root: TreeNode) -> bool:
        def deep(root):
            if not root:
                return 0
            left = deep(root.left)
            if left == -1:
                return -1
            right = deep(root.right)
            if right == -1:
                return -1
            return max(right,left) + 1 if abs(left-right) <= 1 else -1
        return deep(root) != -1
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution.isBalanced(root))