# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return s
        
        s = list(s)
        longest = [s[0]]
        
        for mid in range(len(s)):
            # search for mid with odd
            start, end = mid, mid
            while (start >= 0) and (end < len(s)) and (s[start] == s[end]):
                sub = s[start:end+1]
                start -= 1
                end += 1
                
            if len(sub) > len(longest):
                longest = sub
                
            if len(longest) == len(s):
                return "".join(longest)
                
            start, end = mid, mid + 1
            while (start >= 0) and (end < len(s)) and (s[start] == s[end]):
                sub = s[start:end+1]
                start -= 1
                end += 1
            if len(sub) > len(longest):
                longest = sub
        return "".join(longest)