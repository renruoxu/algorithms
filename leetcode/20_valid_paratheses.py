class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        s = [c for c in list(s) if c in ['(', ')', '{', '}', '[', ']']]
        if len(s) == 0:
            return True
        
        if len(s) == 1:
            return False
        
        # find inner brackets
        idx = 0
        while len(s) > 1:
            if ( (s[idx], s[idx+1]) == ('(', ')') ) or ((s[idx], s[idx+1]) == ('{', '}')) or ((s[idx], s[idx+1]) == ('[', ']')):
                s.pop(idx)
                s.pop(idx)
                idx -= 1
                if idx < 0:
                    idx = 0
            else:
                idx += 1
            
            if idx >= len(s) - 1:
                break
        
        if len(s) > 0:
            return False
        
        return True