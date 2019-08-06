 ###Bubble sort:
###Solution 1:
def bubblesort(lst):
    for n in range(len(lst)-1,0,-1):
        print('level:',n)
        for j in range(n):
            print('compare:',j)
            if lst[j]>lst[j + 1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    print(lst)
#solution 2:
def bubblesort(lst):
    for n in range(len(lst)):
        print('level:',n)
        for j in range(len(lst)-1-n):
            print('compare:',j)
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    print(lst)
Time complexity: O(n^2)
Space complexity: O(1)
