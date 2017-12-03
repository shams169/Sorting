class MaxHeap(object):

    def __init__(self, items=[]):
        super().__init__()
        self.heap=[0]

        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1 )


    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) -  1)

    def peek(self):

        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max  = self.heap.pop()
        else:
            max = False
        return max


    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):

        parent = index // 2;
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1

        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left

        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return (str(self.heap[0:len(self.heap)]))


def main():
    A =  MaxHeap([95, 3, 21])
    A.push(10)
    A.push(4)
    A.push(34)
    A.push(78)
    A.push(2)
    A.push(9)
    A.push(17)
    print(A)
    A.pop()
    print(A)

if __name__ == '__main__':
    main()

