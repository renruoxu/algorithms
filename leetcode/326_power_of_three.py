import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        if n == 1:
            return True
        x = round(math.log(n) / math.log(3))
        if 3 ** x == n:
            return True
            
        return False
