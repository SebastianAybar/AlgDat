import math
import sys


def merge_sort(arr):
    if len(arr) > 1:  # Zeile 2
        # Finde den Mittelpunkt des Arrays und teile es in zwei Hälften
        mid = len(arr) // 2  # Zeile 4
        left_half = arr[:mid]  # Zeile 5
        right_half = arr[mid:]  # Zeile 6

        # Rekursives Sortieren beider Hälften
        merge_sort(left_half)  # Zeile 9
        merge_sort(right_half)  # Zeile 10

        i = j = k = 0  # Zeile 12

        # Zusammenführen der beiden Hälften
        while i < len(left_half) and j < len(right_half):  # Zeile 15
            if left_half[i] < right_half[j]:  # Zeile 16
                arr[k] = left_half[i]  # Zeile 17
                i += 1  # Zeile 18
            else:
                arr[k] = right_half[j]  # Zeile 20
                j += 1  # Zeile 21
            k += 1  # Zeile 22

        # Überprüfen, ob noch Elemente im linken Teil übrig sind
        while i < len(left_half):  # Zeile 25
            arr[k] = left_half[i]  # Zeile 26
            i += 1  # Zeile 27
            k += 1  # Zeile 28

        # Überprüfen, ob noch Elemente im rechten Teil übrig sind
        while j < len(right_half):  # Zeile 30
            arr[k] = right_half[j]  # Zeile 31
            j += 1  # Zeile 32
            k += 1  # Zeile 33

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Test des Mergesort-Algorithmus
if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print("Ursprüngliches Array:")
    print_list(arr)
    merge_sort(arr)
    print("Sortiertes Array:")
    print_list(arr)
