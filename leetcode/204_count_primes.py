class Solution(object):
    def countPrimes(self, n):
        """
        Time limit exceed
        """
        if n <= 1:
            return 0
        primes = []
        i = 2
        while i <= n:
            flag = True
            for p in primes:
                if i % p == 0:
                    flag == False
                    break
            if flag: primes.append(i)
            i += 1
        return len(primes)

class Solution(object):
    def countPrimes(self, n):
        """
        Time limit exceed
        """
        if n <= 1:
            return 0
        primes = [True] * n
        i = 2
        while i < n:
            if primes[i]:
                for j in range(2, (n-1) // i + 1):
                    primes[i * j] = False
            i += 1
        return sum(primes)-2