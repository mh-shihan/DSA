#include <iostream>
using namespace std;

int partition(int *arr, int low, int high)
{
    int i = low;
    int j = high;
    int pivot = arr[low];

    while (i < j)
    {
        while (arr[i] <= pivot && i <= high - 1)
        {
            i++;
        }

        while (arr[j] > pivot && j >= low + 1)
        {
            j--;
        }

        if (i < j)
        {
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[low], arr[j]);

    return j;
}

void quickSort(int *arr, int low, int high)
{
    // if (low < high)
    // BASE CASE
    if (low >= high)
        return;

    // PROCESSING
    int pIndex = partition(arr, low, high);

    // RECURSIVE CALL
    quickSort(arr, low, pIndex - 1);
    quickSort(arr, pIndex + 1, high);
}

int main()
{
    int arr[15] = {9, 4, 7, 9, 9, 1, 1, 10, 3, 2, 8, 1, 5, 6, 0};
    int n = 15;
    quickSort(arr, 0, n - 1);

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}
