from random import randint


def BubbleSort(data):

    size = len(data)

    for i in range(size):
        for j in range(1, size):
            if(data[j-1] > data[j]):
                data[j - 1] , data[j] = data[j],data[j - 1]
        #print(data)


def main():
    data = [randint(1,100) for i in range(10)]
    BubbleSort(data)


if __name__ == '__main__':
    main()