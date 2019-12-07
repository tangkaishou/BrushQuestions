

# 通过切片的方法

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                t = t[t.index(i)+1:]
            else:
                return False
        return True

# 作者：wuqing-array
# 链接：https://leetcode-cn.com/problems/is-subsequence/solution/python3-qie-pian-by-wuqing-array/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。