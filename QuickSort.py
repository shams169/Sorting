from random import randint

def Partition(A, start, end):
    pIndex = start
    pivot = A[end]

    for i in range(start, end):
        if (A[i] <= pivot):
            swap(A, i, pIndex)
            pIndex += 1
    swap(A, end, pIndex)

    return pIndex

def RandomizedPartition(A, start, end):
    pIndex = randint(start, end)
    swap(A, pIndex, end)
    return Partition(A, start, end)



def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def QuickSort(A, start, end):
    if (start < end):
        #pIndex = Partition(A, start, end)
        pIndex = RandomizedPartition(A, start, end)
        QuickSort(A, start, pIndex - 1)
        QuickSort(A, pIndex + 1, end)
    return A


def main():
    A = [7, 2, 1, 6, 8, 5, 3, 4]

    print(QuickSort(A, 0, len(A) - 1))
    # print(Partition(A, 0,7))


if __name__ == '__main__':
    main()
