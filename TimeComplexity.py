# Constant Time (O(1))
def constant_time_operation(arr):
    return arr[0]  # Always takes the same amount of time

# Logarithmic Time (O(log n))
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Linear Time (O(n))
def linear_time_operation(arr):
    for element in arr:
        print(element)

# Linearithmic Time (O(n log n))
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quadratic Time (O(n^2))
def quadratic_time_operation(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

# Exponential Time (O(2^n))
def exponential_time_operation(n):
    if n <= 1:
        return n
    return exponential_time_operation(n-1) + exponential_time_operation(n-2)
