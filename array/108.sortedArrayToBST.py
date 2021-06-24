class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sortedArrayToBST(nums):
        def build(start_index,end_index):
            if start_index > end_index:
                return None
            mid_index = (start_index + end_index) //2
            root = TreeNode(nums[mid_index])
            root.left = build(start_index,mid_index-1)
            root.right = build(mid_index+1,end_index)                
            return root
        return build(0,len(nums)-1)
nums = [-10,-3,0,5,9]
Solution.sortedArrayToBST(nums)