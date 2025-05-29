#hashing Map/Set

arr = [ 1, 2, 0, 4] # [1,2,-3,4] also try with this array

def subarrayWithZeroSum(arr):
    current_sum = 0
    seen_sum = set()
    for num in arr:
        current_sum += num
        if current_sum == 0 or current_sum in seen_sum: 
            return True
        seen_sum.add(current_sum)
    return False

print(subarrayWithZeroSum(arr))

#When you reach the element 0, the current_sum increases by 0 — so if before adding it the sum wasn’t zero or repeated, now it could be zero.
#Since the element itself is zero, current_sum == 0 becomes true at that point.