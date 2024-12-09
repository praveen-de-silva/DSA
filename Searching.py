# Sequencial Search

def seqSearchIter(arr,  item):
    pos = 0
    found = False

    while pos<len(arr) and not found:
        if arr[pos]==item:
            found=True
            break
        pos += 1

    if found:
        return True
    return False


##arr = [1,2,3,4,5]
##print(recSearch(arr, 41))
            
def seqSearchRec(arr, item):
    if len(arr)==0:
        return False
    if arr[0]==item:
        return True

    return recSearch(arr[1:], item)


##print(recSearch(arr, 4))

# =============
# Binary Search
# =============

def seqBinSearch(arr, item):
    first = 0
    last = len(arr)-1
    found = False

    while first<=last and not found:
        mid = (first + last)//2

        if arr[mid]==item:
            found==True
        elif arr[mid]>item:
            last = mid-1
        else:
            first = mid+1
        

    if found:
        return mid
    return False

def recBinSearch(arr, item):
    if len(arr)==0:
        return False
    mid = len(arr)//2

    if arr[mid]==item:
        return True
    if arr[mid]>item:
        return recBinSearch(arr[:mid], item)
    return recBinSearch(arr[mid+1:], item)

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(recBinSearch(arr, 16))
