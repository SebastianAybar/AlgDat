import sys
import math


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)-1]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Beispielaufruf
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Unsortierte Liste:", arr)
sorted_arr = quicksort(arr)
print("Sortierte Liste:", sorted_arr)


