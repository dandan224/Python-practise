
class Solution(object):
 def solve(self, array):
   """
   input: int[] array
   return: int[]
   """
   # write your solution here
   """
   for i in range(len(array)-1, 0, -1):
     max_index = 0
     for j in range(i + 1):
       if (array[j] > array[max_index]):
         max_index = j
        
     array[i],array[max_index] = array[max_index],array[i]
     """
   for i in range(len(array)):
     min_index = i
     for j in range(len(array)-1,i,-1):
       if array[j] < array[min_index]:
         min_index = j
     array[i],array[min_index] = array[min_index],array[i]
   return array
