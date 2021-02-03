#-*- codeing = utf-8 -*-
#@Time : 2021/2/3 11:14
#@Author : XJH
#@File : demo3.py
#@Software:PyCharm

# if 34567:
#     print("True")
# else:
#     print("False")

# score=82
# if score>=90 and score<=100:
#     print("本次考试，等级为A")
# elif score>=80 and score<=90:
#     print("本次考试，等级为B")
# else:
#     print("本次考试，等级为E")

# xingbie=1
# dansheng=1
# if xingbie==1:
#     print("男生")
#     if dansheng==1:
#         print("我给你介绍一个吧？")
#     else:
#         print("你给我介绍一个吧")
# else:
#     print("女生")
#     print("......")

import random   #引入随机库
x=random.randint(0,2)
a=input("")
a=int(a)
if a==0:
    print("你的输入为剪刀（%d）" %a)
elif a==1:
    print("你的输入为石头（%d）" %a)
elif a==2:
    print("你的输入为布（%d）" %a)

print("随机生成数字为：%d" %x)
if x==a:
    print("哈哈，你赢了")
elif (x!=a)and(a!=1)and(a!=0)and(a!=2):
    print("哈哈，输入无效")
else:
    print("哈哈，你输了")