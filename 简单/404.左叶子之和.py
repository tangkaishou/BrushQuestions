# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 总和等于左子树的值加上右子树的值，终止条件是当前节点为左子叶或者为空节点。代码如下：
# 递归
# 递归的时候、主要是在哪里累加才好呢？定义变量不可能，每次递归回来都得重新定义新的变量。只能是在return的时候进行累加。
class Solution:
	def sumOfLeftLeaves(self, root):
		"""return int"""
		if not root:
			return 0

		if root and root.left and not root.left.left and not root.left.right:
			# 满足条件的
			# 递归算法在返回处 进行累加，而不是通过定义变量来累加
			return root.left.val + self.sumOfLeftLeaves(root.right)

		return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)



# 迭代方式
# 迭代树主要是终止条件，那么终止条件的选取就尤为重要了。
# 树的遍历有三种，那么这里是前序遍历，那么遍历到的是左叶子节点呢，如果不是左叶子节点而是其的父节点呢。
# 这里通过一个列表的样式来记录遍历的父节点、遍历过的父节点就pop掉，就不用担心迭代的位置到哪里。
class Solution2:
	def sumOfLeftLeaves(self, root):
		"""return int"""
		sum = 0
		if not root:
			return 0

		ans = [root]
		while ans:
			# 每次都是取最后一个来pop掉，然后检查其是否是叶子节点。
			r = ans.pop()
			if r.left and not r.left.left and not r.left.right:
				sum += r.left.val

			if r.left:
				ans.append(r.left)
			if r.right:
				ans.append(r.right)
		return sum
