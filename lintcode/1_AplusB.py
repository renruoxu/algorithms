# http://www.lintcode.com/en/problem/a-b-problem/

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        if a < 0:
            return b - abs(a)
        elif b < 0:
            return a - abs(b)

        while (a & b) != 0:
            a, b = (a & b) << 1, a ^ b
        return a ^ b
