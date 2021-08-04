#从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

#层次遍历BFS，使用队列，非递归
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(root: TreeNode):
        if not root:
            return []
        que,res = [root],[]
        while que:
            tmp = que.pop(0)
            res.append(tmp.val)
            if tmp.left:
                que.append(tmp.left)
            if tmp.right:
                que.append(tmp.right)
        return res

tree = [3,9,20,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution.levelOrder(root))