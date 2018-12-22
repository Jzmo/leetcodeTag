# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.inorder(root,output)     
        return output
    
    def inorder(self,root,output):   
        
        if not root:
            return 
        
        if root.left:
            self.inorder(root.left,output)     
        output.append(root.val)        
        if root.right:
            self.inorder(root.right,output)
            
        return output
            
        