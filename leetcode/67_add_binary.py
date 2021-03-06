# https://leetcode.com/problems/add-binary/description/
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == "":
            return b
        if b == "":
            return a
        
        a = list(a)[::-1]
        b = list(b)[::-1]
        min_len = min(len(a), len(b))
        
        carry = 0
        p = 0
        final = []
        while p < min_len:
            if carry == 0:
                if (a[p] == "0") and (b[p]=="0"):
                    final.insert(0, "0")
                elif (a[p] == "0" and b[p]=="1"):
                    final.insert(0,"1")
                elif (a[p] == "1" and b[p]=="0"):
                    final.insert(0, "1")
                else:
                    final.insert(0, "0")
                    carry = 1
            else:
                if (a[p] == "0") and (b[p]=="0"):
                    final.insert(0, "1")
                    carry = 0
                elif (a[p] == "0" and b[p]=="1"):
                    final.insert(0,"0")
                elif (a[p] == "1" and b[p]=="0"):
                    final.insert(0, "0")
                else:
                    final.insert(0, "1")
            p += 1
            
        if len(a) > min_len:
            while p < len(a):
                if carry == 0:
                    final.insert(0, a[p])
                else:
                    if a[p] == "1":
                        final.insert(0, "0")
                    else:
                        final.insert(0, "1")
                        carry = 0
                p += 1
                        
        if len(b) > min_len:
            while p < len(b):
                if carry == 0:
                    final.insert(0, b[p])
                else:
                    if b[p] == "1":
                        final.insert(0, "0")
                    else:
                        final.insert(0, "1")
                        carry = 0
                p+=1
                        
        if carry == 1:
            final.insert(0, "1")
        return "".join(final)


# simpler solution
class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        indexa = len(a) - 1
        indexb = len(b) - 1
        carry = 0
        sum = ""
        while indexa >= 0 or indexb >= 0:
            x = int(a[indexa]) if indexa >= 0 else 0
            y = int(b[indexb]) if indexb >= 0 else 0
            if (x + y + carry) % 2 == 0:
                sum = '0' + sum
            else:
                sum = '1' + sum
            carry = (x + y + carry) / 2
            indexa, indexb = indexa - 1, indexb - 1
        if carry == 1:
            sum = '1' + sum
        return sum
        
        