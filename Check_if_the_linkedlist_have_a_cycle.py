###Check if the linkedlist have a cycle:
Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
 def checkCycle(self, head):
   """
   input: ListNode head
   return: boolean
   """
   # write your solution here
   slow = fast = head
   # why fast.next???
   while slow and fast and fast.next:
     slow = slow.next
     fast = fast.next.next
     if slow == fast:
       print 'found'
       return True
   return False
