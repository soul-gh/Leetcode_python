#输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

#递归
#后序遍历，最后一个数是根结点，从前向后遍历数组，找到第一个大于根结点的数，其左边为左子树，右边为右子树。若出现右子树里儿子大于父亲则为假。
class Solution:
    def verifyPostorder(postorder):
        if  not postorder:
            return True
        root = postorder[-1]
        n = len(postorder)
        for i in range(n):
            if postorder[i] > root:
                break
        left = postorder[:i]
        right = postorder[i:n-1]
        for _ in right:
            if _ < root:
                return False
        return Solution.verifyPostorder(left) and Solution.verifyPostorder(right)

num = [4, 8, 6, 12, 16, 14, 10] 
print(Solution.verifyPostorder(num))