##Linked list insert at index
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
 def insert(self, head, index, value):
   """
   input: ListNode head, int index, int value
   return: ListNode
   """
   # write your solution here
   if index < 0:
     return None
   fake_head = ListNode(None)
   fake_head.next = head
   node = ListNode(value)
   
   if index > 0:
     insert_place = self.insert_by_index(head, index)
   elif index == 0:
     insert_place = fake_head
   if insert_place is None:
     return fake_head.next
   node.next = insert_place.next
   insert_place.next = node
   return fake_head.next


 def insert_by_index(self, head, index):
   if not head or index < 0:
     return None
   for _ in range(index-1):
       head = head.next
       if not head:
         return None
   return head
