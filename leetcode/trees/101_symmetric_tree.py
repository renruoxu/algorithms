# https://leetcode.com/problems/symmetric-tree/description/

# go throught both left subtree and right subtree, and compare them
class Solution(object):
    def __init__(self):
        self.left = []
        self.right = []

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        left = root.left
        right = root.right
        self.helper(left, key="l")
        self.helper(right, key="r")

        print self.left
        print self.right

        return (self.left == self.right)


    def helper(self, root, key):
        if root == None:
            if key == "l":
                self.left.append(None)
            else:
                self.right.append(None)
            return None

        if key == "l":
            self.left.append(root.val)
            self.helper(root.left,key)
            self.helper(root.right,key)

        elif key == "r":
            self.right.append(root.val)
            self.helper(root.right, key)
            self.helper(root.left, key)

# traversal throught subtree and break if found different
class Solution(object):
    def __init__(self):
        self.left = []
        self.right = []

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        left = root.left
        right = root.right
        return self.isMirror(left, right)


    def isMirror(self, left, right):
        if (left==None) and (right == None):
            return True
        elif (left==None) or (right==None):
            return False

        if (left.val) != (right.val):
            return False

        else:
            return (self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left))
        
