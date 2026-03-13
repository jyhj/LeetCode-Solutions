"""
题意: 计算时针与分针的最小夹角。
思路1: 转为比例角度计算差值。
复杂度: 时间 O(1), 空间 O(1)。
思路2: 直接用度数公式计算。
复杂度: 时间 O(1), 空间 O(1)。
"""

# Time:  O(1)
# Space: O(1)

class Solution:
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        angle1 = (hour % 12 * 60.0 + minutes) / 720.0
        angle2 = minutes / 60.0
        diff = abs(angle1 - angle2)
        return min(diff, 1.0 - diff) * 360.0


class Solution2:
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_angle = (hour % 12) * 30.0 + minutes * 0.5
        minute_angle = minutes * 6.0
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360.0 - diff)
