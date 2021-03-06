##Merge sort:
class Solution(object):
 def mergeSort(self, array):
   """
   input: int[] array
   return: int[]
   """
   # write your solution here
   # base case:
   if len(array) == 0 or len(array) == 1:
     return array
   middle = len(array)/2
   left = self.mergeSort(array[:middle])
   right = self.mergeSort(array[middle:])
   return self.merge(left, right)
 def merge(self, array1, array2):
   i=j = 0
   result = []
   while i < len(array1) and j < len(array2):
     if array1[i] < array2[j]:
       result.append(array1[i])
       i += 1
     else:
       result.append(array2[j])
       j +=1
     #print result
   while i < len(array1):
     result.append(array1[i])
     i += 1
   while j < len(array2):
     result.append(array2[j])
     j += 1
   return result
