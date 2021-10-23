#实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

#Z字形打印。

#两个栈
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(root: TreeNode):
        if not root:
            return []
        res = []
        stack1,stack2 = [root],[]
        while stack1 or stack2:
            tmp_res = []
            while stack1:
                node = stack1.pop()
                tmp_res.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            if tmp_res:        
                res.append(tmp_res)

            tmp_res = []
            while stack2:
                node = stack2.pop()
                tmp_res.append(node.val)
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
            if tmp_res:
                res.append(tmp_res)
        return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution.levelOrder(root))
                