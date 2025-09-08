#Sorting Algorithm Time Complexity Comparision

import random
import time

#selection sort

def selection_sort(arr):
    a = arr[:]
    n = len(a)
    
    for i in range (n):
        min_index = i 
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
                a[i], a[min_index], a[j]
                
        return a 
    
#insertion sort   

def insertion_sort(arr):
    a = arr[:]
    for i in range (1, len(a)):
        key = a[i]
        j = i - 1
        
        while j >=0 and a[j] > key:
            a[j+1] = a[j]         
            j -= 1
            a[j+1] = key
        return a   


#merge sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    result = [] 
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j]) 
            j += 1
        
        #append remaining elements from left and right
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result  
    

#quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot] 
    right = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]
    
    return quick_sort(left) + mid + quick_sort(right)


def generating_lists():
    
    size = [1000,1000,10000]
    lists = {n: [random.randint(0, 10**6) for _ in range (n)] for n in size}
    return lists

#measuring time complexity

def measure_time(func, arr):
    start= time.time()
    func(arr)
    end= time.time()
    return end - start

list = generating_lists()

algorithms = {
    "Selection sort": selection_sort,
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
    "Quick sort": quick_sort
}


for n, arr in list.items():
    print(f"/List size = {n}")
    for name, func in algorithms.items():
        if n > 1000 and name in ["Selection sort", "Insertion sort"]:
            print(f"{name}: skipped")
            continue
        time_taken = measure_time(func,arr)
        print(f"{name}: {time_taken: .5f} seconds")
