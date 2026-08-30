# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        result = []
        q = deque([root])
        flag=True
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                level.append(node.val)
                if node.right:
                    q.append(node.right)
                
            if not flag:
                level.reverse()   
            
                    
            result.append(level)
            flag=not flag
        
        return result