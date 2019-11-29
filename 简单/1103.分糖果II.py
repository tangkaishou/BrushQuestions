"""

输入：candies = 7, num_people = 4
输出：[1,2,3,1]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0,0]。
第三次，ans[2] += 3，数组变为 [1,2,3,0]。
第四次，ans[3] += 1（因为此时只剩下 1 颗糖果），最终数组变为 [1,2,3,1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distribute-candies-to-people
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for i in range(num_people)]
        x = 1
        while candies > 0:
            for i in range(num_people):
                if candies > x:
                    ans[i] += x
                    candies -= x
                    x += 1
                else:
                    ans[i] += candies
                    candies = 0
        return ans