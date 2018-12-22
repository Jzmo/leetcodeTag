# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack,output = [root],[]
        
        while stack:
            _root = stack.pop()
            output.append(_root.val)
            if _root.left:
                stack.append(_root.left)
            if _root.right:
                stack.append(_root.right)
                
        return output[::-1]