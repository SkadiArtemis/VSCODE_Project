# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
      def kthSmallest(self, root: TreeNode, k: int) -> int:
        buff = list()
        while root or buff:
            while root:
                buff.append(root)
                root = root.left    # searching for small nodes
            
            root = buff.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right