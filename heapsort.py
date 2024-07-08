def heapsort(arr):
    n = len(arr)

    # Build a Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Swap the first element with the last element and heapify
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1 
    right = 2 * i + 2  

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)



arr = [16, 14, 10, 8, 7, 9]
print("Eingabearray = ", arr)
heapsort(arr)
print("Sorted array is:", arr)
