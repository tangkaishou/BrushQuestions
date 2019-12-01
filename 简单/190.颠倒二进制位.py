
class Solution:
	def reverseBits(self, n: int) -> int:
		res = bin(n)[2:]
		res = res.zfill(32)
		res = res[::-1]
		return int(res, base=2)

# 作者：shun-27
# 链接：https://leetcode-cn.com/problems/reverse-bits/solution/shi-shang-zui-chai-pythonjie-fa-by-shun-27/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。