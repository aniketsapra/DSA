#hashing Map/set

arr = [2,3,7,11,15]

def twoSumProblem(arr, target):
    map = {}
    for i, value in enumerate(arr):
        compliment = target - value
        if compliment in map:
            return (map[compliment], i)     #returning index of compliment and current index
        map[value] = i                      #storing value and index in map
    return None

print(twoSumProblem(arr, 9))