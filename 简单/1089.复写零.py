"""

输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
"""

# 在当前列表中操作
class Solution:
	def duplicateZeros(self, arr: List[int]) -> None:
		"""
		Do not return anything, modify arr in-place instead.
		"""
		pos, N = 0, len(arr)
		while pos < N:
			if arr[pos] == 0:
				arr.insert(pos + 1, 0)
				arr.pop()
				pos += 1
			pos += 1
