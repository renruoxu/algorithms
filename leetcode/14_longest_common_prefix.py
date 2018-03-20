class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        strs = [list(s) for s in strs]
        longest = strs[0]
        
        for s in strs:
            if len(s) == 0:
                return ""
            
            if len(s) < len(longest):
                longest = longest[:len(s)]
                
            
            for i in range(min(len(s), len(longest))):
                if s[i] != longest[i]:
                    longest = longest[:i]
                    break
            
        return "".join(longest)