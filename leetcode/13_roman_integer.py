class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I":1,
                      "V":5,
                      "X":10,
                      "L":50,
                      "C":100,
                      "D":500,
                      "M":1000}
        if s == "":
            return 0
        
        s == list(s)
        
        if len(s) == 1:
            return roman_dict[s[0]]
        
        n = 0
        curr = 0
        while curr < len (s) - 1:
            if roman_dict[s[curr]] < roman_dict[s[curr+1]]:
                n -= roman_dict[s[curr]]
            else:
                n += roman_dict[s[curr]]
            curr += 1
            
        n += roman_dict[s[curr]]
        return n
        
        