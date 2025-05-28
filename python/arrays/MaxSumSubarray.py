# max sum of a subarray of size k
# SLIDING_WINDOW approach

arr = [1,2,3,4,5,6,7]

def MaxSumSubarray(arr, k):
    maxSum = 0
    windowSum = 0
    for i in range(k):
        windowSum += arr[i]
    for i in range(k,len(arr)):
        windowSum = windowSum + arr[i] - arr[i-k] #add next subtract previous
        maxSum = max(maxSum, windowSum)
    return maxSum

print(MaxSumSubarray(arr,3))