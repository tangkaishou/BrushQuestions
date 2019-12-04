
class Solution:
	def isPowerOfTwo(self, n):
		for i in range(n):
			if 2 ** i == n:
				return True
			elif 2 ** i > n:
				return False