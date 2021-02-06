#-*- codeing = utf-8 -*-
#@Time : 2021/2/3 16:53
#@Author : XJH
#@File : demo4.py
#@Software:PyCharm

# a=2
# for i in range(a):
#     print(i)

# for i in range(1,10,3):
#     print(i)

# for i in range(-10,-100,-30):
#     print(i)

# name="chengdu"
# for x in name:
#     print(x,end="\t")

# a=["aa","bb","cc","dd"]
# for i in range(len(a)):
#     print(i,a[i])


# i=0
# while i<5:
#     print("当前是第%d次执行循环"%(i+1))
#     print("i=%d"%i)
#     i+=1

# i=0
# sum=0
# while i<100:
#     i=i+1
#     sum=sum+i
#
# print("1-100求和的sum=%d"%sum)

# i=0
# while i<10:
#     i=i+1
#     print("-"*30)
#     if i==5:
#         continue  #结束本次循环
#     print(i)

i=1
while i<10:
    for z in range(1,i+1):
        print("%d*%d=%d"%(i,z,i*z),end="\t")
    print("\n")
    i=i+1
