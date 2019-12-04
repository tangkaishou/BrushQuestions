

# 语法学习
# from collections import Counter
# Counter 的对象可以用 & 来求交集、保留value为最小的那个记录
import collections
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 极简算法
        A = sum(s==g for s,g in zip(secret,guess))
        B = sum((collections.Counter(secret)&collections.Counter(guess)).values())-A
        return "{A}A{B}B".format(A=A,B=B)

# 作者：arrylee
# 链接：https://leetcode-cn.com/problems/bulls-and-cows/solution/mei-you-bi-zhe-geng-jian-ji-de-suan-fa-liao-by-arr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。