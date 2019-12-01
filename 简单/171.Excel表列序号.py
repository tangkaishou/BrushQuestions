class Solution(object):
    def titleToNumber(self, s):
        ans = 0
        for i, c in enumerate(s):
            ans = ans*26 + ord(c)-ord('A')+1
        return ans

# 作者：ljt-4
# 链接：https://leetcode-cn.com/problems/excel-sheet-column-number/solution/python-jie-fa-by-ljt-4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


import functools
class Solution:
    def titleToNumber(self, s: str) -> int:
        return functools.reduce(lambda x, y: x * 26 + y, [ord(a) - 64 for a in s ])
#
# 作者：powcai
# 链接：https://leetcode-cn.com/problems/excel-sheet-column-number/solution/26jin-zhi-zhuan-shi-jin-zhi-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。