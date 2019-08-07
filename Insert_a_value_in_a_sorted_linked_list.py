####Insert a value in a sorted linked list.  
#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
 def insert(self, head, value):
   """
   input: ListNode head, int value
   return: ListNode
   """
   # write your solution here
   fake_head = ListNode(None)
   fake_head.next = head
   new_node = ListNode(value)
   curr = head
   if head == None:
     head = new_node
     new_node.next = None
   elif  head.val >= value:
     new_node.next = head
     fake_head.next = new_node
     head = new_node
   elif curr.next == None and head.val < value:
     curr.next = new_node
     new_node.next = None
   else:
     while curr.next and curr.next.val < value:
       curr = curr.next
     new_node.next = curr.next
     curr.next = new_node
    
    
   return head
