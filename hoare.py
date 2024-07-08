import sys
import math


def hoare_partition(arr, low, high):
    pivot = arr[low]  # Pivot-Element (kann auch anders gewählt werden)
    i = low - 1
    j = high + 1

    while True:
        # Bewege i nach rechts
        i += 1
        while arr[i] < pivot:
            i += 1
        
        # Bewege j nach links
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        # Wenn sich i und j überschreiten, beende die Partitionierung
        if i >= j:
            return j

        # Tausche Elemente bei i und j
        arr[i], arr[j] = arr[j], arr[i]

# Beispielaufruf für Quicksort mit Hoare-Partition
def quicksort(arr, low, high):
    if low < high:
        p = hoare_partition(arr, low, high)
        quicksort(arr, low, p)
        quicksort(arr, p + 1, high)

# Beispielaufruf
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Unsortierte Liste:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Sortierte Liste:", arr)
