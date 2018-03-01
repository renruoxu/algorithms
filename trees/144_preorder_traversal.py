# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.preorder_array = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        self.traversal(root)
        return self.preorder_array

    def traversal(self, root):
        if root == None:
            return

        self.preorder_array.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
