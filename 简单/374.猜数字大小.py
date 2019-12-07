

def guess(num):
    pass


class Solution(object):
    def guessNumber(self, n):
        left = 1
        right = n
        while left < right:
            # mid = left + (right - left) // 2    # 这里如果整型很大的话、会出现溢出为负数。
            mid = (left + right) >> 1
            if guess(mid) == 1:
                # 中位数比猜的数小，因此比中位数小的数包括中位数都不是目标元素
                left = mid + 1
            else:
                right = mid
        # 最后剩下的数一定是所求，无需后处理
        return left

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/guess-number-higher-or-lower/solution/shi-fen-hao-yong-de-er-fen-cha-zhao-fa-mo-ban-pyth/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。