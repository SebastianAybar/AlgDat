import sys
import math

def quicksort(arr, low, high):
    if low < high:
        # pi ist die Partitionierungsstelle, arr[pi] ist jetzt am richtigen Platz
        pi = partition(arr, low, high)
        
        # Rekursiv sortieren der Elemente vor und nach der Partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Pivot wird als letztes Element gewählt
    i = low - 1        # Index des kleineren Elements

    for j in range(low, high):
        # Wenn das aktuelle Element kleiner oder gleich dem Pivot ist
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Tauschen

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Beispielaufruf
array = [10, 7, 8, 9, 1, 5]
n = len(array)
quicksort(array, 0, n - 1)
print("Sortiertes Array:", array)
