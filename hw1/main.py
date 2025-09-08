#Sorting Algorithms Comparison

import random, time

# selection sort 

def selection_sort(arr):
    a = arr[:]                    
    n = len(a)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]   # do the swap after scanning
    return a

# insertion sort

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key                           
    return a

# merge sort 

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
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def generating_lists():
    sizes = [1000, 10000, 100000]
    return {n: [random.randint(0, 10**6) for _ in range(n)] for n in sizes}

def measure_time(func, arr, repeats=1):
    start = time.perf_counter()
    for _ in range(repeats):
        func(arr)
    end = time.perf_counter()
    return (end - start) / repeats

data_sets = generating_lists()

algorithms = {
    "Selection sort": selection_sort,
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
    "Quick sort": quick_sort
}

for n, arr in data_sets.items():
    print(f"/List size = {n}")
    for name, func in algorithms.items():
        
        t = measure_time(func, arr)
        print(f"{name}: {t:.5f} seconds")
