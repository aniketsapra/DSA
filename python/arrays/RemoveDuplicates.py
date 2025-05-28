#sorted array
#TWO_POINTER Approach
#gets number of unique elements

nums = [1,1,2,2,3,4,4]

def RemoveDuplicates(nums):
    unique_index = 0
    for i in range(len(nums)):
        if nums[unique_index] != nums[i]:
            unique_index += 1
            nums[unique_index] = nums[i]
    return unique_index + 1
    
print(RemoveDuplicates(nums))