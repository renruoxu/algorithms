# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.path = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        self.helper(root)
        return self.path

    def helper(self, root):
        if root == None:
            return

        self.inorderTraversal(root.left)
        self.path.append(root.val)
        self.inorderTraversal(root.right)
