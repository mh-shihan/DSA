#include <iostream>
using namespace std;

void insertionSort(int arr[], int n)
{
    int i = 0;
    while ( i < n)
    {
        int j = i;

        while (j > 0 && arr[j - 1] > arr[j])
        {
            int temp = arr[j - 1];
            arr[j - 1] = arr[j];
            arr[j] = temp;
            j--;
        }

        i++;
    }
}

void printingArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}

int main()
{
    int arr[5] = {64, 25, 12, 22, 11};
    insertionSort(arr, 5);
    printingArray(arr, 5);

    return 0;
}