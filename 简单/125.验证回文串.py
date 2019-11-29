
"""
示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp=''.join(re.findall(r'[A-Za-z0-9]', s)).lower()
        l,r=tmp[0:len(tmp)//2],tmp[len(tmp)//2:len(tmp)]
        return l==r[::-1] or l==r[::-1][:-1]

# 作者：sethGu
# 链接：https://leetcode-cn.com/problems/valid-palindrome/solution/pythonshuang-zhi-zhen-by-sethgu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。