# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        queue=deque()
        ans1=0
        queue.append(root)
        while queue:
            node=queue.popleft()
            if node.left:
                if not node.left.left and not node.left.right:
                    ans1+=node.left.val
                else:
                    queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans1