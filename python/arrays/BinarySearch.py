arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #for sorted arrays only

print(arr)

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2 # integer division= //, float division = /
        if arr[mid] == target:
            return f"value found at index {mid}"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "not found"

print(binarySearch(arr, 10))  # Output: value found at index 9
# to get index of the value 


#recursiveBinarySearch
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def recursiveBinarySearch(arr, target, left = 0, right = len(arr)-1):
    if left > right:
        return "Case Not Found"
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursiveBinarySearch(arr, target, mid + 1, right)
    else:
        return recursiveBinarySearch(arr, target, left, mid - 1)

# Make sure this is NOT indented
print(recursiveBinarySearch(arr, 10))  # Output: 9
