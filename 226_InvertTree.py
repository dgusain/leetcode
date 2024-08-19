# 226: Invert Tree
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = 0
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        # rec DFS
        '''
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        '''
        # iter BFS
        if not root:
            return root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root
    

