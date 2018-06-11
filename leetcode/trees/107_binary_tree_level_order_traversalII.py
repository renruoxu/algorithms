# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        self.results = []

        if not root:
            return self.results

        level_nodes = [root]

        while level_nodes:
            new_nodes = []
            self.results.append([n.val for n in level_nodes])

            for n in level_nodes:
                if n.left: new_nodes.append(n.left)
                if n.right: new_nodes.append(n.right)
            level_nodes = new_nodes
        return list(reversed(self.results))
