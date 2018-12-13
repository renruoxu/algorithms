# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def traversal(self, node, path, result):
        path.append(str(node.val))
        
        if node.left is None and node.right is None:
            result.append("->".join(path))
            path.pop()
            return
        
        if node.left:
            self.traversal(node.left, path, result)
        
        if node.right:
            self.traversal(node.right, path, result)
        path.pop()

        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        result = []
        self.traversal(root, [], result)
        return result
        