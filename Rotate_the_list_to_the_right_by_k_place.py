#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
 def rotateKplace(self, head, n):
   """
   input: ListNode head, int n
   return: ListNode
   """
   # write your solution here
   class Solution(object):
 def rotateKplace(self, head, n):
   """
   input: ListNode head, int n
   return: ListNode
   """
   # write your solution here
   if not head:
     return
   # get the size of the linkedlist
   curr = head
   #current = head
   size = 1
   while curr.next:
     curr = curr.next
     size += 1
   # find the tail of the linkedlist
   curr.next = head
  
   #k = n % size
   prelen = size - n% size - 1
  
   pre = head
   while prelen:
     pre = pre.next
     prelen -= 1
   head = pre.next
   pre.next = None
   return head
