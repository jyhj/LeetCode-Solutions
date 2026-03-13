"""
题意: 若某员工在一小时内使用门禁 >= 3 次则触发告警，返回所有告警员工名（字典序）。
思路1: 按姓名分组后排序时间，用滑窗统计 60 分钟内次数。
复杂度: 时间 O(n log n), 空间 O(n)。
思路2: 排序后只需检查任意连续三次是否在 60 分钟内。
复杂度: 时间 O(n log n), 空间 O(n)。
"""

# Time:  O(nlogn)
# Space: O(n)

import collections


class Solution:
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        THRESHOLD = 3
        name_to_times = collections.defaultdict(list)
        for name, hour_minute in zip(keyName, keyTime):
            hour, minute = map(int, hour_minute.split(":"))
            name_to_times[name].append(hour * 60 + minute)
        names = []
        for name, times in name_to_times.items():
            times.sort()
            left = 0
            for right, time in enumerate(times):
                while time - times[left] > 60:
                    left += 1
                if right - left + 1 >= THRESHOLD:
                    names.append(name)
                    break
        names.sort()
        return names


# Time:  O(nlogn)
# Space: O(n)
class Solution2:
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        name_to_times = collections.defaultdict(list)
        for name, hour_minute in zip(keyName, keyTime):
            hour, minute = map(int, hour_minute.split(":"))
            name_to_times[name].append(hour * 60 + minute)
        result = []
        for name, times in name_to_times.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    result.append(name)
                    break
        result.sort()
        return result
