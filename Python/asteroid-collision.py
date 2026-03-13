"""
题意: 模拟小行星碰撞，返回最终状态。
思路1: 用栈处理相向碰撞。
复杂度: 时间 O(n), 空间 O(n)。
思路2: 同上，写法不同。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(n)

class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result = []
        for x in asteroids:
            if x > 0:
                result.append(x)
                continue
            while result and 0 < result[-1] < -x:
                result.pop()
            if result and 0 < result[-1]:
                if result[-1] == -x:
                    result.pop()
                continue
            result.append(x)
        return result


# Time:  O(n)
# Space: O(n)
class Solution2:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result = []
        for x in asteroids:
            while result and x < 0 < result[-1]:
                if result[-1] < -x:
                    result.pop()
                    continue
                elif result[-1] == -x:
                    result.pop()
                break
            else:
                result.append(x)
        return result
