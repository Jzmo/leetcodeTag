# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True    
        return self.isValidNode(root, float('-inf'), float('inf'))
        
    def isValidNode(self,node,lower_bnd,upper_bnd):
            if not node:
                return True
            
            if lower_bnd < node.val < upper_bnd:
                return self.isValidNode(node.left,lower_bnd, node.val) and self.isValidNode(node.right,node.val, upper_bnd)
            else:
                return False
            