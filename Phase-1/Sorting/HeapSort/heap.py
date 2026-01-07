class Heap: 
    # Insert element into the heap
    def insert(self,value): 
        # Rebuild heap to ensure valid heap state before inserting
        self.buildHeap()
        
        index = self.size
        self.arr.append(value)
        self.size += 1

        while(index > 0):
            parent = (index-1)//2
            if (self.arr[parent]<self.arr[index]):
                self.arr[parent],self.arr[index] = self.arr[index],self.arr[parent]
                index = parent
            else:
                return

    
    # Heapify the subtree rooted at target index
    def heapify(self,target, heapSize):
        largest = target
        left = 2 * target +1
        right= 2 * target +2

        if (left< heapSize and self.arr[left]>self.arr[largest]):
            largest = left
        if (right< heapSize and self.arr[right]>self.arr[largest]):
            largest = right

        if (largest != target):
            self.arr[target],self.arr[largest] = self.arr[largest],self.arr[target]
            self.heapify(largest, heapSize)


    # Extract the maximum element from the heap
    def extract(self):
        if (self.size == 0):
            return

        self.arr[0],self.arr[self.size -1] = self.arr[self.size-1], self.arr[0]
        self.size -= 1

        self.heapify(0,self.size)


    # Perform heap sort on the array
    def heapSort(self):
        n = self.size

        while (n>1):
            self.arr[0],self.arr[n-1] = self.arr[n-1],self.arr[0]
            n -= 1
            self.heapify(0, n)
    

    # Build the heap from the current array
    # range(start, stop, step)
    def buildHeap(self):
        for i in range((self.size -1)//2, -1, -1):
            self.heapify(i, self.size)
        

    # Build the heap from the current array
    def __init__(self, items=[], ):
        self.arr = items
        self.size = len(self.arr)
        if len(self.arr) > 0:
            self.buildHeap()


    # Print the current state of the heap
    def printHeap(self):
        printArr = []
        for i in range(self.size):
            printArr.append(self.arr[i])
        print(printArr)
       

array = [50,70,40,10,20, 100]
h = Heap(array)
print("initial heap")
h.printHeap()

h.heapSort()
print("after Heap Sort")
h.printHeap()

h.insert(80)
print("after inserting 80")
h.printHeap()

h.extract()
print("after extracting max")
h.printHeap()

print("Heap Size: ", h.size)

