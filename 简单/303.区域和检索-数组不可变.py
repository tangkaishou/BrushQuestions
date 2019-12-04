# 动态规划
class NumArray:

	def __init__(self, nums):
		self.dp = nums[:]
		for i in range(1, len(self.dp)):
			self.dp[i] += self.dp[i - 1]

	def sumRange(self, i: int, j: int) -> int:
		return self.dp[j] - self.dp[i - 1] if i > 0 else self.dp[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)