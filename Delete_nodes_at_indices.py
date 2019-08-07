 Delete nodes at indices:
Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
 def deleteNodes(self, head, indices):
   """
   input: ListNode head, int[] indices
   return: ListNode
   """
   # write your solution here
   if not head:
     return
   new_head = head
   for i, index in enumerate(indices):
     new_head = self.deleteIndex(new_head, index-i)
     if not new_head:
       return
   return new_head

 def deleteIndex(self, head, index):
   if not head or index < 0:
     return
   fake_head = ListNode(None)
   fake_head.next = head
   curr = head
   if index == 0:
     fake_head.next = curr.next
     head = curr.next
   else:
     prev_node = self.searchbyindex(head, index-1)
     if prev_node is None or prev_node.next is None:
       return fake_head.next
     remove_node = prev_node.next
     prev_node.next = remove_node.next
     remove_node.next = None
   return fake_head.next

 def searchbyindex(self, head, index):
   if not head or index <0:
     return
   for _ in range(index):
     head = head.next
     if not head:
       return
   return head
