'''
    选择排序

'''

'''
    第一种解法：
        1、找出数组（old li）中最小的数据
        2、将最小的数据添加到新数组（New li）中
        3、将旧数组（old li）中的数据删除
    
    该写法缺点：
        空间复杂度：创建了俩个数组，比较浪费
        时间复杂度：O（n*n）
'''

def min_index(arr:list):
    min_index_tmp = 0 #临时最小值索引
    min_value = arr[0]  # 将数组第一个元素看作最小值

    for j in  range(len(arr)):

        if arr[j]  <  min_value:
            min_value = arr[j]
            min_index_tmp = j

    return  min_index_tmp




arr = [3,5,2,1,4,7,6,9,8]
arr_new = []
for i in range(len(arr)):


    minValueIndex = min_index(arr)
    arr_new.append(arr.pop(minValueIndex))
print(arr)
print(arr_new)


'''
    第二种解法：
        1、将数组（arr）中的第一个元素看作为最小的数字，循环len(arr) -1 趟
        2、从i+1，len(arr) 称之为无序区
        3、最关键的是需要知道最小值索引，然后进行替换
'''
arr = [3,5,2,1,4,7,6,9,8]
for i in range(len(arr)-1):
    min_indexInArr = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_indexInArr]:
            min_indexInArr =  j
    arr[i],arr[min_indexInArr] = arr[min_indexInArr],arr[i]

print(arr)







