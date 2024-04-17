#Run the Kadane's Algorithm with Brute Force
#Find a non-empty subarray with the largest sum.
#Tutorial From this video: https://neetcode.io/courses/advanced-algorithms/0 
nums = [4,-1,2,-7,3,4]

def kadane_brute_force(nums):

    max_sum = 0 
    for i in range(len(nums)): 
        curr_sum = 0 
        for j in range(i,len(nums)): 
            curr_sum += nums[j]
            max_sum = max(max_sum,curr_sum)
    
    return max_sum 

#test the result
#res = kadane_brute_force(nums) 
#print(res)

#improve Kadane's Algo with only one pass: 
#This will Use Linear Time for Caculating the current_sum 
#The main ideas here is that as long as we have the currsum < 0, we will just begin again 
#There is one counter keep track of the current sum and another pointer keeps track of 
#max sum 
#Reduce to the Complexity to the Linear Time 
def Kadane(nums):

    max_sum = 0
    curr_sum = 0 
    
    for i in nums: 
        curr_sum = max(curr_sum,0)
        curr_sum +=i
        max_sum = max(curr_sum,max_sum)
    
    return max_sum 

#max_sum = Kadane(nums)
#print(max_sum)

#The sliding Window Problem is very similar to the 
#This Slide Window is also Variable 
def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R 

    return [maxL, maxR]
