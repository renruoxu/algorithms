#https://leetcode.com/problems/sqrtx/description/
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or (x==1):
            return x

        start = 0
        end = x
        mid = (start + end) / 2

        while (start < end - 1):
            mid_square = mid * mid
            if mid_square == x:
                return mid

            if mid_square < x:
                start = mid
            else:
                end = mid
            mid = (start + end) / 2

        return start

# newton raphson's method

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r
