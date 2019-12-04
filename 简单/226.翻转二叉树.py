class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


# 递归
class Solution:
	def invertTree(self, root):
		if not root:
			return
		else:
			# 左右子树的位置交换就可以了
			root.left, root.right = root.right, root.left  # 主要是这里转换
			root.left = self.invertTree(root.left)
			root.right = self.invertTree(root.right)
		return root