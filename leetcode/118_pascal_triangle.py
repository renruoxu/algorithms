# https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        result = [[1], [1,1]]
        last_row = [1,1]
        for i in range(3, numRows + 1):
            this_row = [1]
            for j in range(len(last_row) - 1):
                this_row.append(last_row[j] + last_row[j+1])
            this_row.append(1)
            last_row = this_row
            result.append(this_row)
        return result

class Solution2(object):
    def generate(self, numRows):
        """solution from the discussion"""
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]