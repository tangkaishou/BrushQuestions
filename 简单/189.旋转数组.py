class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        nums[:]=nums[n-k:]+nums[:n-k]

# 作者：zhu_shi_fu
# 链接：https://leetcode-cn.com/problems/rotate-array/solution/san-ci-fan-zhuan-fu-yi-xie-pythonicde-jie-fa-pytho/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
