Delete node at index:

Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
 def deleteNode(self, head, index):
   """
   input: ListNode head, int index
   return: ListNode
   """
   # write your solution here
   if not head or index < 0:
     return
   fake_head = ListNode(None)
   fake_head.next = head
   curr = fake_head

   if index == 0:
     head = head.next
     head = None
    
      
   for _ in range(index):
     curr = curr.next
     if not curr:
       return fake_head.next
## *****
   if curr is None:
     return fake_head.next
   if curr.next is None:
     return fake_head.next
  
   remove_node = curr.next
   if remove_node.next is None:
     curr.next = None
   next = remove_node.next
   remove_node.next = None
   curr.next = next
   # why following code doesn't work????
   #curr.next = curr.next.next
   # curr.next.next = None
  
   return fake_head.next
