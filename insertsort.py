#Insertion Sort
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

def main():
    eingabe = input("Gib Zahlen mit Komma getrennt ein: ")
    array = [int(x) for x in eingabe.split(',')]
    array_sorted = insertion_sort(arr=array)
    print("deine Liste wurde sortiert: " + str(array_sorted))
    
if __name__ == '__main__':
    sys.exit(main())