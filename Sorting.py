# --------------------
# Bubble(Sinking) Sort
# --------------------
#   * rapidly compair each pair of adjacent items
#     and swap them if they are wrong order.
#   * timeComplexity  : O(n^2)
#     spaceComplexity : O(1)  

def bubbleSort(array):
    '''sort the array using Bubble Sort Algorithm'''
    size = len(array)
    
    for j in range(size-1):    
        for i in range(size-1-j):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        

##arr1 = [7,2,1,6,5,4,3]
##
##bubbleSort(arr1)
##print(arr1)


# --------------------
# Bubble(Sinking) Sort
# --------------------
