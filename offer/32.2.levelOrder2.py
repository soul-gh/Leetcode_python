#从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

#层次遍历BFS，使用队列，非递归.由于要分层，多一层循环和数组tmp_res只记录当前层的数据

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
            cnt = len(que)
            tmp_res = []
            for _ in range(cnt):
                node = que.pop(0)
                tmp_res.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tmp_res)
        return res
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution.levelOrder(root))