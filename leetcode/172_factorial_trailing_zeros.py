import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        Numbers that will create trailing zeros is in the format of
        m * 5^k ==> m5^k < n ==>
        """
        count = 0
        if n == 0:
            return 0
        maxk = math.floor(math.log(n) / math.log(5.))
        while maxk >= 1:
            maxm = n / math.pow(5, maxk)
            count += math.floor(maxm)
            maxk -= 1
        return int(count)
