#输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
#**先序遍历确定根节点，再在中序遍历中找到左右子树。 再利用先序遍历分割**

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(preorder, inorder):
        if preorder == []:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = Solution.buildTree(preorder[1:idx+1],inorder[:idx])
        root.right = Solution.buildTree(preorder[idx+1:],inorder[idx+1:])
        return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
node = Solution.buildTree(preorder,inorder)

def print_pretree(node):
    if node == None:
        return
    print(node.val)
    print_pretree(node.left)
    print_pretree(node.right)

def print_intree(node):
    if node == None:
        return
    print_intree(node.left)
    print(node.val)
    print_intree(node.right)

print_pretree(node)
print('\n')
print_intree(node)
