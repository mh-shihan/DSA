#include <iostream>
using namespace std;

int peakElementIndex(int arr[], int size) {
    if(size == 0) return 0; 
    if(arr[0] > arr[1]) return 0;
    if(arr[size -1] > arr[size - 2]) return size - 1;

    int start = 1;
    int end = size - 2;
    

    while (start <= end)
    {
       int mid = start + (end - start) / 2;

       if(arr[mid] > arr[mid - 1] && arr[mid] > arr [mid + 1]) {
           return mid;
       }
         else if(arr[mid] > arr[mid - 1]) {
              start = mid + 1;
         }
         else {
              end = mid - 1;}
    }

    return -1;
}



int main()
{
    int arr[] = {1, 3, 20, 4, 1, 0};
    int size = sizeof(arr) / sizeof(arr[0]);

    int peakIndex = peakElementIndex(arr, size);
    cout << "Peak element index: " << peakIndex << endl;

    return 0;
}