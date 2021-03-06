##Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def reverseKGroup(self, head, k):
    """
    input: ListNode head, int k
    return: ListNode
    """
    # write your solution here
    if not head:
      return
    f_head = ListNode(None)
    f_head.next = head
    start = f_head
    while start.next:
      end = start
      for i in range(k - 1):
        end = end.next
        if end.next == None:
          return f_head.next
      res = self.reverse(start.next, end.next)
      start.next =res[0]
      start = res[1]
    return f_head.next
    


  # define a reverse function
  def reverse(self, start, end):
    fake_head = ListNode(None)
    fake_head.next = start
    while fake_head.next != end:
      tmp = start.next
      start.next = tmp.next
      tmp.next= fake_head.next
      fake_head.next = tmp
    return [end, start]
