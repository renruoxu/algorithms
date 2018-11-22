class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        map_dict = {}
        mapped_chars = set()
        s = list(s)
        t = list(t)
        for i in range(len(s)):
            if s[i] not in map_dict:
                if t[i] not in mapped_chars:
                    map_dict[s[i]] = t[i]
                    mapped_chars.add(t[i])
                else:
                    return False
            elif s[i] in map_dict and (map_dict[s[i]] != t[i]):
                return False
        return True