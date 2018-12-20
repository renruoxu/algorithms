class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        mapper = {}
        str = str.split(" ")
        if len(pattern) != len(str):
            return False
        
        for word, v in zip(str, list(pattern)):
            if v in mapper and mapper[v] != word:
                return False
            elif (v not in mapper) and (word in mapper.values()):
                return False
            mapper[v] = word
        return True