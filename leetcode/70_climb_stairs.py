# https://leetcode.com/problems/climbing-stairs/description/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        onestep = 2
        twostep = 1
        step = 3

        while (step <= n):
            currstep = onestep + twostep
            onestep, twostep = currstep, onestep

            step += 1
        return currstep
