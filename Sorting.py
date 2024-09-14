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
##bubbleSort(arr1)
##print(arr1)


# --------------
# Selection Sort
# --------------

#   * rapidly find the minimum of unsorted part
#     and moveit to the sorted part.
#   * timeComplexity  : O(n^2)
#     spaceComplexity : O(1)

def selectionSort(array):
    '''sort the array using Selection Sort Algorithm'''
    size = len(array)

    for j in range(size-1):
        tempMinIndex = j

        for i in range(j+1, size):
            if array[i]<array[tempMinIndex]:
                tempMinIndex = i
                
        array[j], array[tempMinIndex] = array[tempMinIndex], array[j]
    
##arr1 = [7,6,5,1,2,3,4]
##selectionSort(arr1)
##print(arr1)


# --------------
# Insertion Sort
# --------------

#   * take the first element of the unsorted part and insert it
#     at the correct position of the sorted part.
#   * timeComplexity  : O(n^2)
#     spaceComplexity : O(1)

def insertionSort(array):
    size = len(array)
    
    for j in range(size):
        for i in range(j):
            if array[i]>array[j]:
                tempInsert = array[j]
                array.pop(j)
                array.insert(i, tempInsert)
                break
            print(array[i], end=', ')
        print()

arr1 = [7,6,5,1,2,3,4]
insertionSort(arr1)
print(arr1)
