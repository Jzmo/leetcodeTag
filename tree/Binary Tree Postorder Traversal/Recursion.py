# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.postorder(root,output)
        return output
        
    def postorder(self,root,output):
        
        if not root:
            return
        if root.left:
            self.postorder(root.left,output)
        if root.right:
            self.postorder(root.right,output)
        output.append(root.val)
        
        return output
        
        