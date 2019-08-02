Merge two sorted linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
 def merge(self, one, two):
   """
   input: ListNode one, ListNode two
   return: ListNode
   """
   # write your solution here
   if not one:
     return two
   if not two:
     return one
   if one.val > two.val:
     one,two = two,one
   one.next = self.merge(one.next,two)
   return one
