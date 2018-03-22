# https://leetcode.com/problems/plus-one/description/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = map(str, digits)
        if digits[0] == "-":
            digits = "".join(digits[1:])
            digits = int(digits)
            return map(int, list(str(digits + 1)))
        else:
            digits = "".join(digits[:])
            return map(int, list(str(int(digits) + 1)))
