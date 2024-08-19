# 100. Same tree
from collections import deque
class TreeNode:
    def __init__(self, val=0, left= None, right=None)
        self.val = 0
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode])-> bool:
        # rec DFS
        '''
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        '''
        # iter BFS
        queue1 = deque([p])
        queue2 = deque([q])
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            queue1.append(node1.left)
            queue1.append(node1.right)
            queue2.append(node2.left)
            queue2.append(node2.right)
        
        return not queue1 and not queue2

