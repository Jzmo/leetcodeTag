# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        return self.generate_trees(1,n) if n else []
    def generate_trees(self, start, end):
        if start > end:
            return [None,]
        all_tree = []
        for i in range(start,end+1):
            _left_trees = self.generate_trees(start,i-1)
            _right_trees = self.generate_trees(i+1,end)
            for l in _left_trees:
                for r in _right_trees:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    all_tree.append(node)
        return all_tree
            
        