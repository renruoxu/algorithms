import math
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # turn into binary
        binary = []
        i = 0
        while n > 0:
            binary.append(n % 2) 
            n = n / 2
        binary = binary + [0] * (32 - len(binary))

        reversed_n = 0
        for i, d in enumerate(binary[::-1]):
            reversed_n += math.pow(2, i) * d
        return int(reversed_n)


        