# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):        
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        this_layer = [root]
        next_layer = []
        layer = 0
        while True:
            while len(this_layer) > 0:
                this_node = this_layer.pop()
                left = this_node.left
                if left != None:
                    next_layer.append(left)
                right = this_node.right
                if right != None:
                    next_layer.append(right)
                if left == None and (right == None):
                    return layer + 1
            layer += 1
            this_layer, next_layer = next_layer, []

        