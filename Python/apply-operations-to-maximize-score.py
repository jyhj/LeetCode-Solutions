"""
题意: 选择至多 k 次操作最大化乘积得分。
思路1: 统计每个数的质因子数量，单调栈计算贡献区间，再按数值贪心取最大。
复杂度: 时间 O(sqrt(r) + n * (log r + pi(sqrt r)) + k log n), 空间 O(sqrt r + n)。
思路2: 将贡献次数与数值排序后依次取用（去掉堆）。
复杂度: 时间 O(sqrt r + n log n), 空间 O(n)。
"""

# Time:  O(sqrt(r) + n * (logr + pi(sqrt(r))) + klogn) = O(sqrt(r) + n * (logr + sqrt(r)/log(sqrt(r))) + klogn), m is max(k for _, k in queries), pi(n) = number of primes in a range [1, n] = O(n/logn) by prime number theorem, see https://en.wikipedia.org/wiki/Prime_number_theorem
# Space: O(sqrt(r) + n)

import heapq


# number theory, mono stack, greedy, sort, heap
class Solution:
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        def linear_sieve_of_eratosthenes(n):  # Time: O(n), Space: O(n)
            primes = []
            spf = [-1] * (n + 1)  # the smallest prime factor
            for i in range(2, n + 1):
                if spf[i] == -1:
                    spf[i] = i
                    primes.append(i)
                for p in primes:
                    if i * p > n or p > spf[i]:
                        break
                    spf[i * p] = p
            return primes  # len(primes) = O(n/(logn-1)), reference: https://math.stackexchange.com/questions/264544/how-to-find-number-of-prime-numbers-up-to-to-n

        lookup = {}
        def count_of_distinct_prime_factors(x):
            y = x
            if y not in lookup:
                cnt = 0
                for p in primes:
                    if p * p > x:
                        break
                    if x % p != 0:
                        continue
                    cnt += 1
                    while x % p == 0:
                        x //= p
                if x != 1:
                    cnt += 1
                lookup[y] = cnt
            return lookup[y]

        primes = linear_sieve_of_eratosthenes(int(max(nums) ** 0.5))
        scores = [count_of_distinct_prime_factors(x) for x in nums]

        left = [-1] * len(scores)
        stk = [-1]
        for i in range(len(scores)):
            while stk[-1] != -1 and scores[stk[-1]] < scores[i]:  # if multiple such elements exist, choose the one with the smallest index
                stk.pop()
            left[i] = stk[-1]
            stk.append(i)
        right = [-1] * len(scores)
        stk = [len(scores)]
        for i in reversed(range(len(scores))):
            while stk[-1] != len(scores) and scores[stk[-1]] <= scores[i]:
                stk.pop()
            right[i] = stk[-1]
            stk.append(i)

        result = 1
        max_heap = [(-x, i) for i, x in enumerate(nums)]
        heapq.heapify(max_heap)
        while max_heap:
            _, i = heapq.heappop(max_heap)
            c = min((i - left[i]) * (right[i] - i), k)
            result = (result * pow(nums[i], c, MOD)) % MOD
            k -= c
            if not k:
                break
        return result


class Solution2:
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        def linear_sieve_of_eratosthenes(n):
            primes = []
            spf = [-1] * (n + 1)
            for i in range(2, n + 1):
                if spf[i] == -1:
                    spf[i] = i
                    primes.append(i)
                for p in primes:
                    if i * p > n or p > spf[i]:
                        break
                    spf[i * p] = p
            return primes

        primes = linear_sieve_of_eratosthenes(int(max(nums) ** 0.5))
        lookup = {}
        def count_of_distinct_prime_factors(x):
            if x in lookup:
                return lookup[x]
            y, cnt = x, 0
            for p in primes:
                if p * p > x:
                    break
                if x % p:
                    continue
                cnt += 1
                while x % p == 0:
                    x //= p
            if x != 1:
                cnt += 1
            lookup[y] = cnt
            return cnt

        scores = [count_of_distinct_prime_factors(x) for x in nums]
        left = [-1] * len(scores)
        stk = [-1]
        for i in range(len(scores)):
            while stk[-1] != -1 and scores[stk[-1]] < scores[i]:
                stk.pop()
            left[i] = stk[-1]
            stk.append(i)
        right = [-1] * len(scores)
        stk = [len(scores)]
        for i in reversed(range(len(scores))):
            while stk[-1] != len(scores) and scores[stk[-1]] <= scores[i]:
                stk.pop()
            right[i] = stk[-1]
            stk.append(i)

        items = sorted([(nums[i], (i - left[i]) * (right[i] - i)) for i in range(len(nums))], reverse=True)
        result = 1
        for val, cnt in items:
            if k == 0:
                break
            c = min(cnt, k)
            result = (result * pow(val, c, MOD)) % MOD
            k -= c
        return result

