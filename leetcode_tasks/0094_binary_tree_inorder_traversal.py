# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.inorder(res, root)
        return res
    
    def inorder(self, res, root):
        if root == None:
            return
        
        self.inorder(res, root.left)
        res.append(root.val)
        self.inorder(res, root.right)