#include <iostream>
#include <vector>
using namespace std;



    // Standard binary search
    int binarySearch(vector<int> &arr, int start, int end, int target) {
        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (arr[mid] == target) return mid;

            if (arr[mid] < target)
                start = mid + 1;
            else
                end = mid - 1;
        }
        return -1;
    }

    // Find pivot (index of the largest element)
    int peakElementIndex(int arr[], int size) {

        int start = 0, end = size - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            // Check if mid is pivot
            if (mid < end && arr[mid] > arr[mid + 1])
                return mid;

            if (mid > start && arr[mid] < arr[mid - 1])
                return mid - 1;

            // Move left or right
            if (arr[mid] >= arr[start])
                start = mid + 1;
            else
                end = mid - 1;
        }

        return 0; // Array is not rotated
    }

    int search(vector<int>& nums, int target) {

        int n = nums.size();
        int peak = peakElementIndex(nums.data(), n);  // FIXED

        // If target is exactly at pivot
        if (nums[peak] == target)
            return peak;

        // Decide which part to search
        if (target >= nums[0] && target <= nums[peak])
            return binarySearch(nums, 0, peak - 1, target);

        return binarySearch(nums, peak + 1, n - 1, target);
    }

