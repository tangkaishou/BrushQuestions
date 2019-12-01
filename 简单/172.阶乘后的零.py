
"""
之前小红书面试的时候碰到的一道题，没想到又是 leetcode 的原题。这种没有通用解法的题，完全依靠于对题目的分析理解了，自己当时也是在面试官的提示下慢慢出来的，要是想不到题目的点，还是比较难做的。

首先肯定不能依赖于把阶乘算出来再去判断有多少个零了，因为阶乘很容易就溢出了，所以先一步一步理一下思路吧。

首先末尾有多少个 0 ，只需要给当前数乘以一个 10 就可以加一个 0。

再具体对于 5!，也就是 5 * 4 * 3 * 2 * 1 = 120，我们发现结果会有一个 0，原因就是 2 和 5 相乘构成了一个 10。而对于 10 的话，其实也只有 2 * 5 可以构成，所以我们只需要找有多少对 2/5。

我们把每个乘数再稍微分解下，看一个例子。

11! = 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 11 * (2 * 5) * 9 * (4 * 2) * 7 * (3 * 2) * (1 * 5) * (2 * 2) * 3 * (1 * 2) * 1

对于含有 2 的因子的话是 1 * 2, 2 * 2, 3 * 2, 4 * 2 ...

对于含有 5 的因子的话是 1 * 5, 2 * 5...

含有 2 的因子每两个出现一次，含有 5 的因子每 5 个出现一次，所有 2 出现的个数远远多于 5，换言之找到一个 5，一定能找到一个 2 与之配对。所以我们只需要找有多少个 5。

直接的，我们只需要判断每个累乘的数有多少个 5 的因子即可。

作者：windliang
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/xiang-xi-tong-su-de-si-lu-fen-xi-by-windliang-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        p = 0
        while n >= 5:
            n = n // 5
            p += n
        return p


# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         count = 0
#         while n > 0:
#             count += n / 5
#             n = n / 5
#         return count

sol = Solution()
print(sol.trailingZeroes(25))