# 高斯算法 （首项+末项) * 项数 / 2

class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		return len(nums) * (len(nums) + 1) // 2 - sum(nums)
