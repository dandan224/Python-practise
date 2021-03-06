 #Add Two Numbers(linked list))
### Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    input: ListNode l1, ListNode l2
    return: ListNode
    """
    # write your solution here
    
    if not l1:
      return l2
    if not l2:
      return l1
    fake_node = ListNode(None)
    carry = 0
    while l1 or l2:
       fdata = 0 if l1 is None else l1.val
       sdata = 0 if l2 is None else l2.val
       num = fdata + sdata + carry
       carry = int(num / 10)
       num1 = int(num % 10)
       curr = ListNode(num1)
       if fake_node.next is None:
          fake_node.next = curr
          head = curr
       else:
         head.next = curr
         head = head.next
       if l1:
         l1 = l1.next
       if l2:
         l2 = l2.next
    if carry > 0:
      head.next = ListNode(carry)
    return fake_node.next
