###Insertion sort:
##Solution #1:
def insert_num(array,num):
    idx = len(array) - 1
    array.append(num)
    while idx >=0:
        if array[idx] > array[idx + 1]:
            array[idx], array[idx +1] = array[idx+1], array[idx]
        idx = idx - 1
    print(array)
def insertion_sort(array):
    new_array=[]
    for i in range(len(array)) :
      insert_num(new_array,array[i])
    return new_array


