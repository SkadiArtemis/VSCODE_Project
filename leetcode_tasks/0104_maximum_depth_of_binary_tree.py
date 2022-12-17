# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, i):
            if not node:
                if i > self.res: self.res = i
                return
            dfs(node.left, i + 1)
            dfs(node.right, i + 1)
        
        self.res = 0
        dfs(root, 0)
        return self.res