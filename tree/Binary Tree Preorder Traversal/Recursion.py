# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.preorder(root,output)
        return output
    
    def preorder(self, root, output):
        
        if not root:
            return
        output.append(root.val)
        if root.left:
            self.preorder(root.left,output)
        if root.right:
            self.preorder(root.right,output)
            
        return output