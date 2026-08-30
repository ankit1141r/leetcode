# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: 
            return []
        
        result = []
        q = deque([root])
        
        while q:
            sum=0
            size=0
            for i in range(len(q)):
                size+=1
                node = q.popleft()
                sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(sum/size)
        
        return result
