

'''
    二分法查找

'''


def binarySearch(a:list,target):

    lowindex = 0
    highindex = len(a) -1


    while lowindex <= highindex:
        mid = int(lowindex + highindex) // 2
        #print(mid)
        guess = a[mid]

        if guess == target:
            return mid
        if guess > target:
            highindex = mid -1
        if guess < target:
            lowindex = mid + 1
        else:
            return  None






a=[i for i in range(0,10)]
print(binarySearch(a, 4))