###Selection sort linked list
Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
 def selectionSort(self, head):
   """
   input: ListNode head
   return: ListNode
   """
   # write your solution here
   fake_head = ListNode(None)
   fake_head.next = head
   tail = fake_head
   while tail.next:
     prev,curr = tail,tail.next
     min_node,min_node_prev = curr,prev
     while curr:
       if curr.val < min_node.val:
         min_node,min_node_prev = curr, prev
       prev,curr = curr, curr.next
     min_node_prev.next = min_node.next
     min_node.next = tail.next
     tail.next = min_node
     tail = tail.next
   return fake_head.next
