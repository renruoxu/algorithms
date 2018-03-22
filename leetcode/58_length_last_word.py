# https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(" ")
        s = filter(lambda x: x!= "", s)
        if len(s) == 0:
            return 0
        else:
            return len(s[-1])
