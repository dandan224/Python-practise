# solution #1(by using map, the space cost is not O(1)):

Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def findCycle(self, head):
    """
    input: ListNode head
    return: ListNode
    """
    # write your solution here
    if not head:
      return
    s = set()
    curr = head
    while curr:
      if curr in s:
        return curr
      s.add(curr)
      curr = curr.next
    return 

#time complexity:O(n)
#space complexity:O(n)

Solution #2
#1. If a loop is found, initialize slow pointer to head, let fast pointer be at its position.
#2. Move both slow and fast pointers one node at a time.
#3. The point at which they meet is the start of the loop.
Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def findCycle(self, head):
    """
    input: ListNode head
    return: ListNode
    """
    # write your solution here
    if not head or not head.next:
      return
    slow = fast = head
  
    while slow and fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        break
    if slow !=fast:
      return None
    slow = head
    while slow != fast:
      slow = slow.next
      fast = fast.next
    return slow
      
        

#time complexity:O(n)
#space complexity:O(1)


