# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# first solution is much slower
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):        
    def _helper(self, sumroot, root):
        if root == None and (sumroot.val == self.sum):
            self.judge = True
        
        if root:
            if root.left:
                sumroot.left = TreeNode(sumroot.val + root.left.val)
                self._helper(sumroot.left, root.left)
            if root.right:
                sumroot.right = TreeNode(sumroot.val + root.right.val)
                self._helper(sumroot.right, root.right)
            # print self.sum, sumroot.val, self.sum == sumroot.val
            if (root.left == None) and (root.right == None) and sumroot.val == self.sum:
                self.judge = True
        return self.judge
            
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.sum = sum
        self.judge = False
        if root == None:
            return False
        
        sumroot = TreeNode(root.val)
        judge =  self._helper(sumroot, root)
        return judge

class Solution2(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        print sum, root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


if __name__ == "__main__":
    #test case
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    sol = Solution2()
    print sol.hasPathSum(root, 22)
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # sol = Solution()
    # print sol.hasPathSum(root, 1)
        