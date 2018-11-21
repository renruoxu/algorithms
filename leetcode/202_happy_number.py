class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        n = str(n)
        sequence = {}
        while True:
            n = sum([int(d)**2 for d in list(n)])
            if n == 1:
                return True
            else:
                n = str(n)
                if n in sequence:
                    return False
                sequence[n] = True