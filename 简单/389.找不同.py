class Solution:
	def findTheDifference(self, s: str, t: str) -> str:
		from collections import Counter
		sCounter = Counter(s)
		tCounter = Counter(t)

		# 只有一个返回值
		# for i in (tCounter - sCounter):
# 		# 	return i


		# 第二种方式
		return list(tCounter - sCounter)[0]