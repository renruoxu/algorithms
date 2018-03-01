# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return None

        layer = [root]
        serialised = [root.val]

        while len(layer) > 0:
            this_layer = []
            for p in layer:
                left = p.left
                right = p.right
                if left != None:
                    serialised.append(left.val)
                    this_layer.append(left)
                else:
                    serialised.append(None)
                if right != None:
                    serialised.append(right.val)
                    this_layer.append(right)
                else:
                    serialised.append(None)
            layer = this_layer
        return serialised



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == None:
            return None

        root = TreeNode(data[0])

        layer = [root]
        i = 1

        while (len(layer) != 0) and (i < len(data)):
            for p in layer:
                left = data[i]
                i += 1
                right = data[i]
                i += 1
                if left != None:
                    p.left = TreeNode(left)
                    layer.append(p.left)
                if right != None:
                    p.right = TreeNode(right)
                    layer.append(p.right)
                layer = layer[1:]
        return root
