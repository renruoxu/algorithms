# https://leetcode.com/problems/palindrome-number/description/
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n_digits = 0
        x_copy = x
        
        while x_copy > 0:
            x_copy /= 10
            n_digits += 1
        start = 0
        end = n_digits - 1
        
        while (start < end):
            if (x / (10**start) % 10) != (x / (10**end) % 10):
                return False
            else:
                start += 1
                end -= 1
        return True