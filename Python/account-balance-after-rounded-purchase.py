"""
题意: 将消费金额四舍五入到最接近的 10，返回剩余余额（初始 100）。
思路1: (purchase+5)//10*10 进行四舍五入。
复杂度: 时间 O(1), 空间 O(1)。
思路2: 用取模判断离前后 10 的距离。
复杂度: 时间 O(1), 空间 O(1)。
"""

# Time:  O(1)
# Space: O(1)

# math
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        return 100 - (purchaseAmount + 5) // 10 * 10


class Solution2:
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        lower = purchaseAmount - purchaseAmount % 10
        upper = lower + 10
        rounded = lower if purchaseAmount - lower < upper - purchaseAmount else upper
        return 100 - rounded
