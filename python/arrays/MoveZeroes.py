#unsorted array moving zeroes at back
#TWO_POINTER approach

nums = [0,1,0,3,12]

def move_zeroes(nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1
    return nums
