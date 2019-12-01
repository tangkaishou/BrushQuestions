


# 不重复造轮子

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        from collections import Counter
        numDict = Counter(nums)
        for key, value in numDict.items():
            if value > n / 2:
                return key