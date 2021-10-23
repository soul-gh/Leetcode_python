# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

#递归
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(root: TreeNode) -> TreeNode:
        if root == None:
            return
        if root.left and root.right:
            root.left,root.right = root.right,root.left
            Solution.mirrorTree(root.left)
            Solution.mirrorTree(root.right)
        elif root.left:
            root.right = root.left
            root.left = None
            Solution.mirrorTree(root.right)
        else:
            root.left = root.right
            root.right = None
            Solution.mirrorTree(root.left)
        return root

tree = [4,2,7,1,3,6,9]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1) 
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

root = Solution.mirrorTree(root)
def preorder(root):
    if not root:
        return 
    print(root.val)
    preorder(root.left)
    preorder(root.right)
preorder(root)

