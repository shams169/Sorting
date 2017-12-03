from random import randint

def buildMaxHeap(data):
    for i in range(len(data) // 2, -1, -1):
        max_heapify(data, i)
        #print(data)
        #print('---------------------------')
    return data

def max_heapify(A, i):
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def heapSort(A):

    print(A)
    #1 Store the max
    result = []
    l = len(A)
    for i in range(len(A)):
        result.append(A[0])
        A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
        A = A[:len(A)-1]
        #print(A)
        #print('Slice: '+str(A))
        max_heapify(A,0)
        #print("Bottom: "+str(A))

    print("Sorted")
    print(result)


def bottom_down(A, i):

    left  = 2*i + 1
    right = 2*i + 2
    largest = i

    if left < len(A) and A[left] > A[i]:
        A[left], A[i] = A[i], A[left]
        largest = left
    if right < len(A) and A[right] > A[i]:
        A[right], A[i] = A[i], A[right]
        largest= right

    if largest <= (len(A) // 2):
        bottom_down(A, largest)







def main():

    A = [randint(1,9999) for i in range(100)]
    #A = [22, 30, 26, 5, 19, 3, 31, 14, 1, 9]
    print(A)
    A = buildMaxHeap(A)
    print(A)

    heapSort(A)




if __name__ == '__main__':
    main()

