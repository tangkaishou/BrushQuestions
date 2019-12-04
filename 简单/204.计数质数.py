

# 暴力解法超时
# for...else...的用法
class Solution:
	def countPrimes(self, n):
		res = 0
		for i in range(2, n):
			for j in range(2, i):
				if i % j == 0:
					break
			else:
				res += 1
		return res

# 暴力法2
class Solution2:
	def countPrimes(self, n):
		res = 0
		for i in range(2, n):
			for j in range(2, int(i ** 0.5) + 1):
				if i % j == 0:
					break
			else:
				res += 1
		return res






