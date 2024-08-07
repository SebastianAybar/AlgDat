import sys
import math

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)   
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1        

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


array = [8, 2, 3, 4, 5, 9, 7]
n = len(array)
quicksort(array, 0, 4)
print("Sortiertes Array:", array)
