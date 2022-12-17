# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        
        return self.buildBST(nums, 0, len(nums) - 1)

    def buildBST(self, nums, start, end):
        if start > end:
            return None
        
        mid = start + (end - start) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums, start, mid - 1)
        root.right = self.buildBST(nums, mid + 1, end)
        return root