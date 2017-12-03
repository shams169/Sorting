def Partition(A, start, end):
    print("Partition called...")
    print(A[start:end+1])
    pIndex = start
    pivot = A[end]


    for i in range(start, end):
        if(A[i] <= pivot):
            swap(A, i, pIndex)
            pIndex += 1
    swap(A, end, pIndex)
    print("************")
    print(A[start:end+1])
    return pIndex



def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def QuickSort(A, start, end):
    if( start < end ):
        pIndex = Partition(A, start,end)
        QuickSort(A, start, pIndex-1)
        QuickSort(A, pIndex+1, end)
    print("QS: "+str(A))



def main():
    A = [7,2,1,6,8,5,3,4]

    QuickSort(A, 0, len(A)-1)
    # print(Partition(A, 0,7))


if __name__ == '__main__':
    main()