"""示例
输入：[1,1,4,2,1,3]
输出：3
解释：
高度为 4、3 和最后一个 1 的学生，没有站在正确的位置。
"""


class Solution:
	def heightChecker(self, heights: List[int]) -> int:
		# 拿到正确的排序顺序
		right_list = sorted(heights)
		tuple_tt = zip(right_list, heights)
		nums = 0
		for tuple_item in tuple_tt:
			if tuple_item[0] != tuple_item[1]:
				nums += 1

		return nums
