# 104: Max depth of binary tree
from collections import deque
class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = 0
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # sol 1: rec DFS
        '''
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth)+1
        '''
        # sol 2: iter BFS
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
    