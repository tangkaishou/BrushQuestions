"""

刚开始也没看懂题意，看到大佬的思路后猛然明白这是一个阅读理解题。。。奇数之间移动无消耗，偶数之间移动也无消耗，所以可以在无消耗的情况下把筹码都移动到相邻的两个位置上，再进行1消耗的搬运即可，也就是看看奇数和偶数谁更少

作者：wang-wang-wang-23
链接：https://leetcode-cn.com/problems/play-with-chips/solution/python3jian-dan-ming-liao-de-ti-jie-by-wang-wang-w/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        ji = 0
        ou = 0
        for i in chips:
            if i%2 == 0:
                ou+=1
            else:
                ji+=1
        return min(ji,ou)

# 作者：wang-wang-wang-23
# 链接：https://leetcode-cn.com/problems/play-with-chips/solution/python3jian-dan-ming-liao-de-ti-jie-by-wang-wang-w/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。