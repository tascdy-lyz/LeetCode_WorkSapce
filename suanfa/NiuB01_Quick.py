'''
    快速排序

'''





def partion(li:list,left,right):

    tmp = li[left]

    while left < right:


        while li[right] >= tmp:
            right -= 1

        li[left] = li[right]



    li[right] = tmp
