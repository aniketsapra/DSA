arr = [1, 2, 3, 4]
queries = [[1, 3], [0, 3]]

def rangeSums(arr, queries):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[i-1] + arr[i])  # build prefix sum array [1, 3, 6, 10]

    results = []
    for l, r in queries:
        total = prefix[r] if l == 0 else prefix[r] - prefix[l-1]
        results.append(total)

    return results

print(rangeSums(arr, queries))