
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(max_profit, prices[i]-min_price)
        return max_profit
#
# 作者：ljt-4
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/pythonliang-chong-jie-fa-by-ljt-4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。