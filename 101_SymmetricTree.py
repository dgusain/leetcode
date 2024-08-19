# 101: Symmetric tree
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = 0
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # rec DFS
        '''
        def isMirror(t1:TreeNode, t2: TreeNode)->bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        return isMirror(root, root)
        '''
        # iter BFS
        if not root:
            return True
        queue = deque([(root, root)])
        while queue:
            t1, t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        
        return True
    