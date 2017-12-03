def MaxSubArray(data):

    if(len(data)==1):
        return data[0]

    mid = len(data) // 2

    left_Mss = MaxSubArray(data[:mid])
    right_Mss = MaxSubArray(data[mid:])

    leftSum  = -999999
    rightSum = -999999
    ans = 0

    sumArr = sum(data[mid:])
    rightSum = max(rightSum,sumArr)

    sumArr=0
    sumArr= sum(data[:mid])
    leftSum = max(leftSum, sumArr)

    ans = max(left_Mss,right_Mss)
    print(ans, leftSum, rightSum)
    return max(ans, leftSum+rightSum)



data = [3,-2,5,-1]

print("Final :"+str(MaxSubArray(data)))


