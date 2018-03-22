# https://leetcode.com/problems/implement-strstr/description/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        needle_len = len(needle)
        p = 0
        while p <= len(haystack) - len(needle):
            if haystack[p:p+needle_len] == needle:
                return p
            p += 1

        return -1
