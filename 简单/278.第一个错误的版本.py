
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(n):
	pass


class Solution:
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# 二分查找法
		low = 0
		height =  n
		while low < height:
			mid = (low + height) // 2
			if not isBadVersion(mid) and isBadVersion(mid +1):
				return mid + 1
			elif isBadVersion(mid):
				height = mid
			elif not isBadVersion(mid):
				low = mid




