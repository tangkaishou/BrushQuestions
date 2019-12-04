

class Solution:
	def isHappy(self, n):
		n = str(n)
		visited = set()
		while True:
			n = str(sum([int(i) ** 2 for i in n]))
			if n == "1":
				return True
			if n in visited:
				return False # 无限循环
			visited.add(n)


# 第二种解法
# 不快乐数最终会出现 4 16 37 56 89 145 42 20 的循环递归
class Solution:
	def isHappy(self, n):
		while True:
			n = sum([int(i)**2 for i in str(n)])
			if n == 4:
				return False
			if n == 1:
				return True

	