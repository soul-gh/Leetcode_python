#输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

#回溯
#记录答案的path时需要list（path）复制进去，否则path改变，res内的数据也会改变。
#回溯到当前位置pop
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(root: TreeNode, target: int):
        res,path = [],[]
        def search(node,target):
            if not node:
                return 
            path.append(node.val)
            target -= node.val
            if target == 0 and not node.left and not node.right:
                res.append(list(path))
            search(node.left,target)
            search(node.right,target)
            path.pop()
        search(root,target)
        return res

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
print(Solution.pathSum(root,22))
