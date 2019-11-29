"""
输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

递归很耗时间
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n ==1:
            return 1
        elif n ==2:
            return 1
        left = 0
        middle = 1
        right = 1
        for i in range(3, n+1):
            left, middle, right = middle, right, left + middle + right
        return right



# 斐波那契数列
# def feibo(n):
# 	if n == 0:
# 		return 0
# 	elif n ==1:
# 		return 1
#
# 	left, right = 0, 1
# 	for i in range(2, n+1):
# 		left, right = right, left + right
# 	return right
#
# for i in range(10):
# 	print(feibo(i))