# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root: return (0, None)
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 > h2: return (1 + h1, lca1)
            if h1 < h2: return (1 + h2, lca2)
            return (1 + h1, root)
        return helper(root)[1]