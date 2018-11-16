import re
pattern = r'[a-zA-Z0-9]'
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(re.findall(pattern, s)).lower()
        if len(s) <= 1:
            return True
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1 
        return True