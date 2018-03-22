# https://leetcode.com/problems/count-and-say/description/
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            x = self.countAndSay(n-1)
            x = list(x)
            prev = x[0]
            curr = 1
            count = 1
            final_string = []

            while curr < len(x):
                curr_c = x[curr]
                if curr_c == prev:
                    curr += 1
                    count += 1
                    prev = curr_c
                else:
                    final_string.append(str(count))
                    final_string.append(prev)
                    curr += 1
                    prev = curr_c
                    count = 1

            final_string.append(str(count))
            final_string.append(prev)

            return "".join(final_string)
