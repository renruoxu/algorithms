# https://leetcode.com/problems/invert-binary-tree/description/
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        return root

    def helper(self, root):
        if root == None:
            return None

        root.left, root.right = root.right, root.left
        self.helper(root.left)
        self.helper(root.right)
