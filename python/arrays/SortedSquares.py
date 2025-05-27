#sorted array
#two_pointer approach

arr = [-4, -1, 0, 3, 10]

def SortedSquares(arr):
    sortedSq = []
    left = 0
    right = len(arr) - 1
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            sortedSq.insert(0, arr[left] * arr[left])
            left += 1
        else:
            sortedSq.insert(0, arr[right] * arr[right])
            right -= 1
    return sortedSq

print(SortedSquares(arr))