###Quick sort:
class Solution(object):
 def quickSort(self, array):
   """
   input: int[] array
   return: int[]
   """
   # write your solution here
   self.quick_sort(array, 0, len(array) - 1)
   return array
  
 def quick_sort(self, array, start, end):
   from random import randrange
   if start >= end:
     return
   pivot_index = randrange(start, end + 1)
   new_pivot_index = self.partition(array, start, end, pivot_index)
   self.quick_sort(array, start, new_pivot_index - 1)
   self.quick_sort(array, new_pivot_index + 1, end)
  
 
  def partition(self,lst,start,end,pivot_index):
   lst[pivot_index],lst[end] = lst[end],lst[pivot_index]
   store_index = start
   pivot = lst[end]
   for i in range(start, end):
     if lst[i] < pivot:
       lst[i],lst[store_index] = lst[store_index],lst[i]
       store_index += 1
   lst[store_index],lst[end] = lst[end],lst[store_index]
   return store_index
