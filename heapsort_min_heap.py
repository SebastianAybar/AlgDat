def heapsort(arr):
    n = len(arr)

    # Build a min-heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Swap the first element with the last element and heapify
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    smallest = i  # Initialize smallest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is less than root
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # See if right child of root exists and is less than root
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # Swap if needed
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

# Beispielausführung
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Eingabearray = ", arr)
heapsort(arr)
print("Sorted array is:", arr)
