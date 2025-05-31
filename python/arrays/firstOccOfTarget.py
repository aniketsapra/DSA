#binary_search + sort

arr = [1,2,4,4,4,5,6]

def firstOccurenceOfTarget(arr,target):
    left = 0
    right = len(arr)-1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1         #keep moving right pointer to find the first occurrence
        elif arr[mid] < target:
            left = mid + 1          
        else:
            right = mid - 1
    return result
    
print(firstOccurenceOfTarget(arr,4))