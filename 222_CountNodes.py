# 222: count complete tree nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None)
        self.val = 0
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode])-> int:
        if not root:
            return 0
        def get_depth(node:TreeNode)-> int:
            depth = 0
            while node:
                node = node.left
                depth += 1
            return depth
        
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)

        if left_depth == right_depth:
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            return (1 << right_depth) + self.countNodes(root.left)
        

