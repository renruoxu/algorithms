# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_p = []
        path_q = []
        self.find_path(path_p, root, p)
        self.find_path(path_q, root, q)
        
        
        for node in path_p[::-1]:
            if node in path_q:
                return node
        
    def find_path(self, path, root, node):
        if root == None:
            return False
        
        path.append(root)
        
        if root == node:
            return True
        
        if self.find_path(path, root.left, node) or self.find_path(path, root.right, node):
            return True
        
        path.pop()
        return False