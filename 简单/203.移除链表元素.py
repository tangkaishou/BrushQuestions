# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 迭代
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)  # 考虑到头部就是我们要删除的内容、自己构建一个头结点。
        dummy.next = head
        prev = dummy
        last = prev.next
        while last :
            if last.val == val:
                prev.next = last.next
                last = prev.next
            else:
                prev = prev.next
                last = prev.next
        return dummy.next

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/remove-linked-list-elements/solution/di-gui-he-die-dai-by-powcai-6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 递归
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/remove-linked-list-elements/solution/di-gui-he-die-dai-by-powcai-6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

