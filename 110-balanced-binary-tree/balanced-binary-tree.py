# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        self.max_diff = 0
        
        def helper(node, depth):
            if not node:
                return depth
            
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            
            self.max_diff = max(self.max_diff, abs(left - right))
            
            return max(left, right)
            
        helper(root, 0)
        return self.max_diff <= 1