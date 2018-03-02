# http://www.lintcode.com/en/problem/trailing-zeros/

class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        count = 0

        while (n >= 5):
            n = n / 5
            count += n

        return count
