#112: Path Sum
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = 0
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum:int) -> bool:
        # rec DFS
        '''
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        targetSum -= root.val
        return self.hasPathSum(root.left) or self.hasPathSum(root.right)
        '''
        # iter BFS
        if not root:
            return False
        queue = deque([(root, root.val)])
        while queue:
            node, node_sum = queue.popleft()
            if not node.left and not node.right:
                if node_sum == targetSum:
                    return True
            if node.left:
                queue.append((node.left, node.left.val + node_sum))
            if node.right:
                queue.append((node.right, node.right.val + node_sum))
        
        return False
    
