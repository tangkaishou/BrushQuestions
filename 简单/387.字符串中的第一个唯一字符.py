

# 不要重复造轮子
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        sCounter = Counter(s)
        for key, value in sCounter.items():
            if value == 1:
                return s.index(key)
        return -1