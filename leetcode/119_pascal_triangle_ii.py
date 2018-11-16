# https://leetcode.com/problems/pascals-triangle-ii/
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        last_row = [1,1]
        for i in range(2, rowIndex+1):
            print i
            this_row = [1]
            for j in range(len(last_row) - 1):
                this_row.append(last_row[j] + last_row[j+1])
            this_row.append(1)
            last_row = this_row
        return this_row

