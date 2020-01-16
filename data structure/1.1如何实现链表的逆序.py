"""
head->1->2->3->4->5->6->7
head->7->6->5->4->3->2->1
"""
class LNode:
	def __init__(self, val):
		self.data = val
		self.next = None


def Reverse(head):
	if head==None or head.next==None:
		return

	pre = None
	cur = None
	next = None

	# 首节点处理
	cur = head.next
	next = cur.next
	cur.next = None

	pre = cur
	cur = next

	while cur.next != None:
		next = cur.next
		cur.next = pre
		pre = cur
		# cur = cur.next
		cur = next

	cur.next = pre
	head.next = cur



if __name__ == '__main__':
	i = 1
	head = LNode(0)
	head.next = None
	tmp = None
	cur = head

	while i < 2:
		tmp = LNode(i)
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		i += 1

	print('逆序前')
	cur = head.next
	while cur != None:
		print(cur.data, end=' ')
		cur = cur.next
	print()
	Reverse(head)
	print('逆序后')
	cur = head.next
	while cur != None:
		print(cur.data, end=' ')
		cur = cur.next


"""
上面的测试数据如果是 head->1 那么就会抛出错误
"""