from random import randint

def insertion_sort(data):
    count = len(data)

    for i in range(1,count):
        val = data[i]
        for j in range(i):
            if(data[j]>data[i]):
                data[j],data[i] = data[i], data[j]
        #print(data)
    return data

def insertionWithwhile(data):

    for i in range(1, len(data)):
        val = data[i]

        hole = i

        while(hole > 0 and data[hole-1] > val):
            data[hole] = data[hole-1]
            hole = hole -1
        data[hole] = val
    return data
        #print(data)


def main():
    data = [randint(1,100) for i in range(10)]
    print(data)
    print(insertion_sort(data))
    print(insertionWithwhile(data))

if __name__=='__main__':
    main()
