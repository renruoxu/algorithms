# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ld = 0
        self.rd = 0

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        if self.depth(root) == -1:
            return False
        else:
            return True


    def depth(self, root):
        if root == None:
            return 0

        leftDepth = self.depth(root.left)

        if leftDepth == -1:
            return -1

        rightDepth = self.depth(root.right)
        if rightDepth == -1:
            return -1

        if abs(leftDepth-rightDepth) > 1:
            return -1
        else:
            return max(leftDepth, rightDepth) + 1
