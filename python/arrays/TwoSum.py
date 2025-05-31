arr = [2,3,7,13] #finding pair which sums upto target TWO_POINTER approach

def hasPairTwoSum(arr, target):
  left = 0
  right = len(arr) - 1
  while left < right:
    sum = arr[left] + arr[right]
    if sum == target:
      return f"{arr[left]} + {arr[right]} = {sum}"
    elif sum < target:
      left+=1                           #python doesn't support left++ and left--
    else:
      right-=1
  return "no pair"
  
print(hasPairTwoSum(arr,9))


# Sorting Array 
# Two_Pointer
arr = [8, 7, 3, 12, 5]

def hasPairTwoSum(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    print(arr)

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])  # Or (left, right) if you want indices
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    return "No Pair Available"

print(hasPairTwoSum(arr, 10))
