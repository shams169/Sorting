from random import randint

def merge(left, right, data):
    i=0;
    j=0;
    k=0;

    nL = len(left)
    nR = len(right)

    while(i<nL and j < nR):
        if( left[i] < right[j]):
            data[k] = left[i]
            k += 1
            i += 1
        else:
            data[k] = right[j]
            k += 1
            j += 1

    while(i<nL):
        data[k] = left[i]
        k += 1
        i += 1
    while(j<nR):
        data[k] = right[j]
        k += 1
        j += 1



def MergeSort(data):

    if(len(data) > 1 ):
        mid   = len(data) // 2
        left  = data[:mid]
        right = data[mid:]

        MergeSort(left)
        MergeSort(right)

        merge(left, right, data)

    return data




def main():
    data = [randint(1,100) for i in range(10)]
    print(data)
    print(MergeSort(data))

if __name__=='__main__':
    main()