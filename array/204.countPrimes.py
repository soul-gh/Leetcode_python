
class Solution:
    def countPrimes(n):
        is_prime = [1] * n
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
                for j in range(i*i, n, i):
                    is_prime[j] = 0
        return count