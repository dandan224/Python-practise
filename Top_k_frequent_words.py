Top k frequent words:
class Solution(object):
 def topKFrequent(self, combo, k):
   """
   input: string[] combo, int k
   return: string[]
   """
   # write your solution here
  
   freq = {}
   for num in combo:
       if num in freq:
           freq[num] =freq[num] + 1
       else:
           freq[num] = 1
   return sorted(freq.keys(), key = lambda w: -freq[w])[:k]
   Return sorted(freq.keys(),key = lambda w: freq[w],reverse = True)[:k]
