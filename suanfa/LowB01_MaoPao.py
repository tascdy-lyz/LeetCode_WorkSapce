'''
    lOWB 排序 ： 冒泡排序
    冒泡排序
'''

arrlist=[2,343,534,22,44,456]
length =len(arrlist)
for i in range(length):
    print(f"第{i}（索引）圈，值为{arrlist[i]}")
    exchange = False
    for j in range(i,length-i-1):
        print(f"内循环 第{j}（索引）圈，值为{arrlist[j]}")
        if arrlist[j] > arrlist[j+1]:
            arrlist[j],arrlist[j+1] = arrlist[j+1],arrlist[j]
            exchange = True
    if not exchange:
        break
    print(f"第{i}圈，此时列表顺序为{arrlist}")

        #print(f"第{i}（索引）圈，值为{arrlist[i]}")
print(arrlist)