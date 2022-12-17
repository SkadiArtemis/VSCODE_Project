# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return None, 0
            xl, xr = 0, 0
            
            if node.left:
                lca_l, xl = dfs(node.left)
                if lca_l: return lca_l, xl
            if node.right:
                lca_r, xr = dfs(node.right)
                if lca_r: return lca_r, xr
            
            x = xl | xr
            if node.val == p.val: x |= 1
            if node.val == q.val: x |= 2
            
            return (node, x) if x == 3 else (None, x)
        
        return dfs(root)[0]