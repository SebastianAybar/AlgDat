import math
import sys

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key
    return arr


def binary_search(arr, target, start, end):
    if start > end:
        return print("number not found")
    middle = math.floor((start + end) / 2)
    if target == arr[middle]:
        return print("found at index: " + str(middle))
    elif target < arr[middle]:
        return binary_search(arr, target, start, middle-1)
    else:
        return binary_search(arr, target, middle+1, end)
    


def main():
    eingabe = input("Gib Zahlen mit Komma getrennt ein: ")
    array = [int(x) for x in eingabe.split(',')]
    array_sorted = insertion_sort(arr=array)
    print("deine Liste wurde sortiert: " + str(array_sorted))
    target = int(input("nach welcher Zahl suchst du: "))    
    binary_search(array_sorted, target, start=0, end=len(array_sorted)-1)
    
if __name__ == '__main__':
    sys.exit(main())





