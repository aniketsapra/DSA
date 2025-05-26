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