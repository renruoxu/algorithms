import string
letters = list(string.ascii_uppercase)

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        columns = []
        if n == 1:
            return "A"
        while n > 0:
            n -= 1
            mod = n % 26
            columns.append(letters[mod])
            n = (n - mod) / 26
        columns = columns[::-1]
        return "".join(columns)