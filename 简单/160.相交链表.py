

# 拼接法
# [4, 1, 8, 4, 5]
# [5, 0, 1, 8, 4, 5]

# 拼接后
# [4,1, 8, 4, 5, 5, 0, 1, 8, 4, 5]
# [5,0, 1, 8, 4, 5, 4, 1, 8, 4, 5]
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha
#
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/intersection-of-two-linked-lists-shuang-zhi-zhen-l/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。