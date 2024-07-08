import sys
import math


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Beispielaufruf
arr = [5, 8, 7, 6, 9, 4, 3, 2, 1]
print("Unsortierte Liste:", arr)
sorted_arr = quicksort(arr)
print("Sortierte Liste:", sorted_arr)


