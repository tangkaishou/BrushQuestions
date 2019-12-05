
class Solution:
	def isPowerOfTwo(self, n):
		for i in range(n):
			if 2 ** i == n:
				return True
			elif 2 ** i > n:
				return False

# 第二种做法： 2的幂的二进制位只有最高位为1、其他位都为0，   2的幂-1的二进制位只有最高位为0、其他位都是1。 那么他们相与就是 0
class Solution:
	def isPowerOfTwo(self, n):
		return n > 0 and (n & (n-1)) == 0

