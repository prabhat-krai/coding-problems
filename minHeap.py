class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParentId = (len(array) - 2) // 2
        for currentId in reversed(range(firstParentId + 1)):
            self.siftDown(currentId, len(array) - 1, array)
        return array

    def siftDown(self, currentId, endId, heap):
        childOne = currentId*2 + 1
        while(childOne <= endId):
            childTwo = currentId*2 + 2 if (currentId*2 + 2) <  endId else -1
            if (childTwo != -1 and heap[childTwo] < heap[childOne]):
                idToSwap = childTwo
            else:
                idToSwap = childOne
            if(heap[idToSwap] < heap[currentId]):
                self.swap(idToSwap, currentId, heap)
                currentId = idToSwap
                childOne = currentId*2 + 1
            else:
                return

        

    def siftUp(self, currentId, heap):
        parentId = (currentId - 1)//2

        while(currentId > 0 and heap[currentId] < heap[parentId]):
            self.swap(parentId, currentId, heap)
            currentId = parentId
            parentId = (currentId - 1)//2


    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return valueToRemove

    def insert(self, value):
	    self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)
	
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]


MinHeap([2,3,1])
