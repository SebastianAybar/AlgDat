
#include <stdio.h>

// Hauptfunktion zum Ausführen von Heapsort
void heapsort(int arr[], int n) {
    // Build a Max-Heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Swap the first element with the last element and heapify
    for (int i = n - 1; i > 0; i--) {
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }
}

// Funktion zum "Heapify" eines Subtrees mit der Wurzel bei index i
void heapify(int arr[], int n, int i) {
    int largest = i;  // Initialize largest as root
    int left = 2 * i + 1;  // left = 2*i + 1
    int right = 2 * i + 2;  // right = 2*i + 2

    // See if left child of root exists and is greater than root
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // See if right child of root exists and is greater than root
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // Swap and continue heapifying if root is not largest
    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

// Funktion zum Vertauschen von zwei Elementen
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}


// Hilfsfunktion zum Drucken des Arrays
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Beispielmain-Funktion zum Testen des Heapsort-Algorithmus
int main() {
    int arr[] = {16, 14, 10, 8, 7, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Eingabearray = ");
    printArray(arr, n);

    heapsort(arr, n);

    printf("Sorted array is: ");
    printArray(arr, n);
    return 0;
}
