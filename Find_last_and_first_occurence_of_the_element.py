###Find last occurence of the element 
class Solution(object):
 def lastOccur(self, array, target):
   """
   input: int[] array, int target
   return: int
   """
   # write your solution here
   if not array:
     return -1
   left,right=0,len(array) -1
   while left < right -1:
     mid =(left + right)/2
     if array[mid] > target:
       right = mid - 1
     else:
       left = mid
   if array[right] == target:
     return right
   if array[left] == target:
     return left
   return -1
   
#########################  
Find the first occurence of the element
class Solution(object):
 def firstOccur(self, array, target):
   """
   input: int[] array, int target
   return: int
   """
   # write your solution here
   if not array:
     return -1

   left, right = 0, len(array)-1
   while left < right - 1:
     mid = (left + right)/2
     if array[mid] < target:
       left = mid + 1
     else:
       right = mid
   if array[left]==target:
     return left
   if array[right]==target:
     return right
   return -1
