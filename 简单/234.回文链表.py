# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		if not (head and head.next):
			return True

		arr, i = [], 0
		while head:
			arr.append(head.val)
			head = head.next

		j = len(arr) - 1
		while i < j:
			if arr[i] != arr[j]:
				return False
			else:
				i += 1
				j -= 1
		return True
