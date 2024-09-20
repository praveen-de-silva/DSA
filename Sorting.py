import math

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
        key = array[j]
        i = j-1

        while i>=0 and key < array[i]:
            array[i+1] = array[i]
            i -= 1
            
        array[i+1] = key
    return array

##arr1 = [7,6,5,1,2,3,4]
##insertionSort(arr1)
##print(arr1)

# -----------
# Bucket Sort
# -----------

#   * sorting by deviding items to several buckets
#   * timeComplexity  : O(n^2)    ~ In worst case
#                       O(log(n)) ~ In best case
#     spaceComplexity : O(n)

def bucketSort(array):
    '''sort the array using Bucket Sort Algorithm'''
    
    size = len(array)
    countBuckets = round(math.sqrt(size))
    k = countBuckets/max(array)
    buckets = [[] for _ in range(countBuckets)]

    for x in array:
        bucketNo = math.ceil(x * k)
        buckets[bucketNo-1].append(x)

    for bucket in buckets:
        insertionSort(bucket)

    k = 0
    for i in range(countBuckets):
        for j in range(len(buckets[i])):
            array[k] = buckets[i][j]
            k += 1

    return array

# with negative numbers

def bucketSortWithNegNum(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    minValue = min(customList)
    maxValue = max(customList)
    rangeVal = (maxValue - minValue) / numberOfBuckets
 
    buckets = [[] for _ in range(numberOfBuckets)]
 
    for j in customList:
        if j == maxValue:
            buckets[-1].append(j)
        else:
            indexB = math.floor((j - minValue) / rangeVal)
            buckets[indexB].append(j)
    
    sortedArray = []
    for i in range(numberOfBuckets):
        buckets[i] = insertionSort(buckets[i])
        sortedArray.extend(buckets[i])

    customList.clear()
    customList += sortedArray
    return customList

##arr1 = [7,6,5,-33,4,8,9]
##bucketSortWithNegNum(arr1)
##print(arr1)


# ----------
# Merge Sort
# ----------

#   * sorting by deviding items to several buckets
#   * timeComplexity  : O(log(n))
#     spaceComplexity : O(n)


# Method 01

def mergeSort(array):
    # chech if is array already sorted (i.e. : is single element)
    if len(array)>1:    
        mid = len(array)//2 # middle of the array

        # Buckets :
        left_sub_array = array[:mid]
        right_sub_array = array[mid:]

        # sort the buckets recursively
        mergeSort(left_sub_array)
        mergeSort(right_sub_array)

        i = j = k = 0

        # copy data from temporal sub-arrays to merge
        while i<len(left_sub_array) and j<len(right_sub_array):
            if left_sub_array[i] < right_sub_array[j]:
                array[k] = left_sub_array[i]
                i += 1
                k += 1
            else:
                array[k] = right_sub_array[j]
                j += 1
                k += 1

        # copy remaining data of left sub-array
        while i<len(left_sub_array):
            array[k] = left_sub_array[i]
            i += 1
            k += 1

        # copy remaining data of right sub-array
        while j<len(right_sub_array):
            array[k] = right_sub_array[j]
            j += 1
            k += 1


# Method 02

def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = array[l+i]

    for j in range(0, n2):
        R[j] = array[m+1+j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

    print(L, R)

def mergeSort2(array, l, r):
    if l < r:
        m = (l+(r-1))//2
        print(f'in mergeSort1({arr1}, {l}, {m})')
        mergeSort2(array, l, m)
        
        print(f'in mergeSort2({arr1}, {m+1}, {r})')
        mergeSort2(array, m+1, r)
        
        print(f'in merge({arr1}, {l}, {m}, {r})')
        merge(array, l, m, r)

##arr1 = [2,3,4,1]
##mergeSort(arr1)


# ----------
# Quick Sort
# ----------

def swap(array, index_1, index_2):
    array[index_1], array[index_2] = array[index_2], array[index_1]

def pivot(array, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if array[i] < array[pivot_index]:
            swap_index += 1
            swap(array, swap_index, i)

    swap(array, pivot_index, swap_index)
    return swap_index 

def  quickSort(array, left, right):
    if left < right:
        pivot_index = pivot(array, left, right)
        quickSort(array, left, pivot_index-1)
        quickSort(array, pivot_index+1, right)

    return array
    
arr1 = [2,3,4,1]
quickSort(arr1, 0, 3)
