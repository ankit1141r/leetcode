# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            node = q.popleft()
            ans.append(node.val)
            if node.right:
                q.appendleft(node.right)

            if node.left:
                q.appendleft(node.left)

        return ans
            