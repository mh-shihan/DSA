#include <iostream>
#include <vector>
using namespace std;

class Heap {
    public:
    int arr[100];
    int size;

    // Constructor
    Heap(){
        arr[0] = -1;
        size = 0;
    }

    // Insertion in Max Heap
    void insert(int val) {
        size = size + 1;
        int index = size;
        arr[index] = val;

        while (index > 1) {
            int parent = index / 2;

            if (arr[parent] < arr[index]) {
                swap(arr[parent], arr[index]);
                index = parent;
            } else {
                return;
            }
        }
    }

    // Delete from Heap
    void deleteFromHeap() {
        if (size == 0) {
            cout << "Nothing to delete" << endl;
            return;
        }

        // Step 1: Put last element in root
        arr[1] = arr[size];
        size--;

        // Step 2: Take root to its correct position
        int i = 1;
        while (i < size) {
            int leftIndex = 2 * i;
            int rightIndex = 2 * i + 1;

            if (leftIndex <= size && arr[i] < arr[leftIndex]) {
                swap(arr[i], arr[leftIndex]);
                i = leftIndex;
            } else if (rightIndex <= size && arr[i] < arr[rightIndex]) {
                swap(arr[i], arr[rightIndex]);
                i = rightIndex;
            } else {
                return;
            }
        }
    }

    // Print Heap
    void print() {
        for (int i = 1; i <= size; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};


void heapify(int arr[], int n, int i) {
    int largest = i; 
    int left = 2 * i; 
    int right = 2 * i + 1; 

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

int main() {
    Heap h;

    vector<int> vec = {54, 53, 55, 52, 50};

    for (int i = 0; i < vec.size(); i++) {
        h.insert(vec[i]);
    }

    h.print();

    h.deleteFromHeap();
    h.print();

    int arr[] = {-1, 54, 53, 55, 52, 50};
    int n = sizeof(arr) / sizeof(arr[0]);
    for (int i = n/2; i >= 1; i--)
    {
        heapify(arr, n, i);
    }

    cout << "Array representation of Heap after heapify: ";
    for (int i = 1; i < n; i++) {
        cout << arr[i] << " ";
    }cout << endl;
    

    return 0;
}