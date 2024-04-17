#Solve for the simple question, find the length of the longest array 
#with the same value in earch position
def longest_array_v1(nums): 

    l = 0 
    max_length = 0 

    for r in range(len(nums)): 
        if nums[l] == nums[r]: 
            max_length = max(max_length,r-l+1)
        else: 
            l = r
    return max_length 

#The above is my code and the below is from Neetcode website 
def longestSubarray(nums):
    length = 0
    L = 0
    
    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R 
        length = max(length, R - L + 1)
    return length


#test, pass the test 
nums = [4,2,2,3,3,3]
#res=longest_array_v1(nums)
#res_valid = longestSubarray(nums)
#print(res_valid)
#print(res)

#another classic example for sliding window is 
#Find the minimum length subarray, where the sum is greater than or equal to the target. 
#Assume all values are positive.
#This question in the notes are in the leetcode
#https://leetcode.com/problems/minimum-size-subarray-sum/description/
#Input: target = 7, nums = [2,3,1,2,4,3]
#Output: 2
#Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#This problem is very similar but only the constraint is different 
#create the l and r index as two pointers, l is the slow pointer and r is the faster pointer 
#loop through the r 
def minLenSubarray(nums,target): 
    
    j = 0
    currSum = 0 
    minLen = float("inf")

    for i in range(len(nums)): 
        currSum+= nums[i]
        while currSum >= target: 
            minLen = min(minLen,i-j+1)
            currSum -= nums[j]
            j+=1 
    return 0 if minLen == float("inf") else minLen

nums = [2,3,1,2,4,3]
res = minLenSubarray(nums,7)
print(res)
