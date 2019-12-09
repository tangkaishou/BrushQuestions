
# 贪心算法
class Solution:
	def longestPalindrome(self, s: str) -> int:
		from collections import Counter
		ans = 0
		for v in Counter(s).values():
			# 奇数+偶数=奇数。
			ans += v // 2 * 2
			# 只会有第一个是奇数满足 ans%2 == 0 之后的奇数都没有办法加1进去了。
			if ans % 2 == 0 and v % 2 == 1:
				ans += 1
		return ans


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/longest-palindrome/solution/zui-chang-hui-wen-chuan-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。