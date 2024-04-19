#This code is to show how to do binary search 
#Given a Sorted Array, Find the index of the target in an array 
nums = [1,3,4,5,7,8,110,123] 
target = 8 

def binary_search(nums,target): 
    
    low = 0 
    high = len(nums) - 1 

    while low <= high: 
         mid = (low+high)//2 

         if nums[mid] > target: 
              high = mid -1 
         elif nums[mid] < target: 
              low = mid + 1 
         else: 
              return mid 
    
    return -1 

#test the results ;
print(binary_search(nums,target)) 

#guess Number for binary search 

