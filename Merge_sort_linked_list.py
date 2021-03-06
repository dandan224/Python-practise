####Merge sort linked list:
Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
 def mergeSort(self, head):
   """
   input: ListNode head
   return: ListNode
   """
   # write your solution here
   if not head or not head.next:
     return head
   one, two = self.splitInHalf(head)
   one = self.mergeSort(one)
   two = self.mergeSort(two)
   return self.merge(one,two)
    
 def splitInHalf(self, head):
   slow = fast = head
   prev = slow
   while fast and fast.next:
     prev = slow
     slow = slow.next
     fast = fast.next.next
   right_part = prev.next
   prev.next = None
   return head, right_part
 def merge(self, one, two):
   prev = ListNode(None)
   curr = prev
   while one and two:
     if one.val < two.val:
       curr.next = one
       one = one.next
     else:
       curr.next = two
       two = two.next
     curr = curr.next
   if one:
     curr.next = one
   else:
     curr.next = two
   return prev.next
