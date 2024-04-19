#insertion Sort: Take one value and insert into an array to get sorted 
nums= [2,3,4,1,6]  
#This can be loop through first nth element to get sorted 
#For example, make sure, 2, 23, 234 are sorted, this can be solved recursive and iteratively 
#This is also can be solved by two pointers 
#Create i for anchoring the number to be sorted 

def insertionSort(nums):

    for i in range(1,len(nums)): 
        j = i-1 
        while (j>=0 and nums[j] > nums[j+1]): 
            temp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = temp 
            j-=1 
        
    return nums 

#res=insertionSort(nums)
#print(res)

#For the insertion sort, the O(n) can be large, which is the worst case can be O(n^2)

#Merge Sort: 
#Split the array in approximately equal half 
#individual elements for us to sort 
#Use the divide and conquer to solve the problem 
#Use the TWo Pointer Technique to do the merge sort 
# Implementation of MergeSort
def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    # The middle index of the array
    m = (s + e) // 2

    # Sort the left half
    mergeSort(arr, s, m)

    # Sort the right half
    mergeSort(arr, m + 1, e)

    # Merge sorted halfs
    merge(arr, s, m, e)
    
    return arr

#merge function after recusive call 
# Merge in-place
def merge(arr, s, m, e):
    # Copy the sorted left & right halfs to temp arrays
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i = 0 # index for L
    j = 0 # index for R
    k = s # index for arr

    # Merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # One of the halfs will have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

nums = [5,2,3,1]
res=mergeSort(nums, 0, 3)
print(res)


 #Quick Sort is the same but it is just with the Pivot
 # Implementation of QuickSort
def quickSort(arr, s, e):
    if e - s + 1 <= 1:
        return

    pivot = arr[e]
    left = s # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot
    
    # Quick sort left side, the left-1, because the pivot does not need extra effort to be sorted, that is why it 
    #should be totally excluded them 
    quickSort(arr, s, left - 1)

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr
       
