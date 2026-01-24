import heapq

def kLargestElements(arr, k):
    minHeap = []

    for n in arr:
        heapq.heappush(minHeap, n)
        
        if(len(minHeap) > 2):
            heapq.heappop(minHeap)
    
    return minHeap


def kLargestSorting(arr, k):
    arr.sort()

    # arr[start : end]
    # If start is negative, Python counts from the end of the list.
    # Meaning of -k
        # '-1' → last element
        # '-2' → second last element
        # '-k' → k-th element from the end
    return arr[-k:]


arr = [3, 2, 1, 5, 6, 4, 9]
k = 2
print(kLargestElements(arr, k))