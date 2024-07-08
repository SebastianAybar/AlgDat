import sys
import math

def quicksort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        pivot = arr[mid]
        pi = partition(arr, low, high, pivot)
        
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high, pivot):
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    
    return low - 1


arr = [4, 2, 6, 1, 5, 9, 7, 3, 8]
quicksort(arr, 0, len(arr) - 1)
print(arr)
