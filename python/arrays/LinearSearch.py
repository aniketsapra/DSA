arr = [10, 99, 100, 40]
print(arr)

def linearSearch(target, arr):
    for i, value in enumerate(arr):
        if value == target:
            return f"value found at {i} index"
    return "not exist"

print(linearSearch(10, arr))



#one liner ver of linear search
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(arr)
print(len(arr))

try:
    index = arr.index(10)
    print(f"value found at index {index}")
except ValueError:
    print("not found")
