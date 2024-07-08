import sys 
import math


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  
    i = low + 1       

    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[low], arr[i - 1] = arr[i - 1], arr[low] 
    return i - 1



# Beispielaufruf
array = [4, 2, 3, 1]
n = len(array)
quicksort(array, 0, n - 1)
print("Sortiertes Array:", array)
