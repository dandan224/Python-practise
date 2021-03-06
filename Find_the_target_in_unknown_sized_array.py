####Find the target in unknown sized array
class Solution(object):
 def search(self, dic, target):
   """
   input: Dictionary dic, int target
   return: int
   """
   # write your solution here
   # get the boundary first by using start * 2
   start = 1
   while dic.get(start) and dic.get(start) < target:
     start *= 2
   left,right = 0,start
   while left <= right:
     mid = (left + right)/2
     if dic.get(mid) < target:
       left = mid + 1
     elif dic.get(mid) > target:
       right = mid - 1
     else:
       return mid
   return -1
