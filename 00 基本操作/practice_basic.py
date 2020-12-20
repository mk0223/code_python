"""
习题1：有4个数字：1，2，3，4。能组成多少个互不相同且不重复的三位数？分别是多少？
"""
# sum = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != j) and (i != k) and (j != k):
#                 a = i * 100 + j * 10 + k
#                 print(a)
#                 sum += 1
# print('总共可以组成{}个不重复的数字。'.format(sum))

"""
习题2: 企业发放的奖金根据利润提成，利润低于或等于10万元时，奖金提成10%；
利润在10~20万元之间，高于10万元的按照7.5%提成；
利润在20~40万元之间，高于20万元的按照5%提成；
利润在40~60万元之间，高于40万元的按照3%提成；
利润在60~100万元之间，高于60万元的按照1.5%提成；
利润超过100万元时，高于100万元的按照1%提成；
从键盘输入当月利润，求当月的奖金是多少？
"""
# while 1:
#     k = input('请输入本月利润总额(退出请输入"q")：')
#     if k.lower() == 'q':
#         break
#     try:
#         i = float(k)
#         arr = [1000000, 600000, 400000, 200000, 100000, 0]
#         rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
#         result = 0
#         for idx in range(0, 6):
#             if i > arr[idx]:
#                 result += (i - arr[idx]) * rat[idx]
#                 i = arr[idx]
#         print('本月的奖金总额是：{}元。'.format(result))
#     except Exception:
#         print('输入的金额格式不对，请重新输入。')

"""
习题3：输入三个整数x,y,z；请把这三个整数从小到大排列。
"""
# while 1:
#     x = input('请输入第一个整数(退出请输入"q")：')
#     if (x.lower()) == 'q':
#         break
#     y = input('请输入第二个整数(退出请输入"q")：')
#     if (y.lower()) == 'q':
#         break
#     z = input('请输入第三个整数(退出请输入"q")：')
#     if (z.lower()) == 'q':
#         break
#     try:
#         fX = float(x)
#         fY = float(y)
#         fZ = float(z)
#         L1 = [fX, fY, fZ]
#         L2 = sorted(L1)
#         print('这三个整数从小到大排列是：{}<{}<{}。'.format(L2[0], L2[1], L2[2]))
#     except Exception:
#         print('输入的数字格式不对，请重新输入。')

"""
习题4：将一个列表的数据复制到另一个列表中。
"""
# F1 = open('read.txt', 'r')
# F2 = open('write.csv', 'w')
# L1 = F1.readlines()
# for item in L1:
#     F2.write(item)
# F1.close()
# F2.close()

"""
习题5：暂停一秒输出，并格式化当前时间。使用time模块的sleep()函数。
"""
# import time
# print(time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time())))
# time.sleep(1)
# print(time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time())))
# time.sleep(2)
# print(time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time())))

"""
习题6：打印出所有的”水仙花数“，所谓”水仙花数“是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个”水仙花数“，因为153 = 1**3 + 5**3 + 3**3。
"""
# sum = 0
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             if (i ** 3 + j ** 3 + k ** 3 == i * 100 + j * 10 + k * 1):
#                 print(i * 100 + j * 10 + k * 1)
#                 sum += 1
# print('总共有{}个水仙花数。'.format(sum))

"""
习题7：输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数。
"""
# s1 = input('请输入任意一串字符：')
# aCount = 0
# nCount = 0
# bCount = 0
# oCount = 0
# for i in s1:
#     if i.isalpha():
#         aCount += 1
#     elif i.isdigit():
#         nCount += 1
#     elif i.isspace():
#         bCount += 1
#     else:
#         oCount += 1
# print('该字符串中总共有{}个中英文字母。'.format(aCount))
# print('该字符串中总共有{}个数字。'.format(nCount))
# print('该字符串中总共有{}个空格。'.format(bCount))
# print('该字符串中总共有{}个其他字符。'.format(oCount))

"""
习题8：一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下。求它在第十次落地时，共经过多少米？第十次反弹多高？
"""
# sum = 100
# dis = 0
# for i in range(1, 11):
#     sum += dis * 2
#     dis = (100 / (2 ** i))
# print('第十次落地时，共经过{:.2f}米。'.format(sum))
# print('第十次反弹{:.5f}米高。'.format(dis))

"""
习题9：利用递归方法求5！
"""
# result = 1
# for i in range(1, 6):
#     result *= i
# print('5! =', result)

# def factorial(j):
#     result2 = 0
#     if j == 0:
#         result2 = 1
#     else:
#         result2 = j * factorial(j-1)
#     return result2
# for k in range(10):
#     print('{}!={}'.format(k, factorial(k)))

"""
习题10：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
"""
# def reversePrint(s, i):
#     if i == 0:
#         return ''
#     return s[i-1] + str(reversePrint(s, i-1))
#
# while 1:
#     s = input('请输入一个字符串(退出请输入”q“):')
#     if s.lower() == 'q':
#         break
#     print('该字符串的逆向字符串是：', reversePrint(s, len(s)))

"""
习题11：按逗号分隔列表
"""
# L1 = [1, 2, '3']
# s1 = ','.join(str(s) for s in L1)
# print(s1)

"""
习题12：将一个数组逆序输出
"""
# L1 = [1, 2, 3, 4, 5]
# L2 = sorted(L1, reverse=True)
# print(L2)

"""
习题13：两个3行3列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
"""
# import numpy as np
# m1 = np.random.randint(0, 10, (3, 3))
# m2 = np.random.randint(0, 10, (3, 3))
# m3 = m1 + m2
# print('m1:\n', m1)
# print('m2:\n', m2)
# print('m1+m2:\n', m3)

"""
习题14：匿名函数求和
"""
# f = (lambda x, y: x+y)
# print(f(2, 3))

"""
习题15：查找字符串的位置
"""
# s1 = 'fdjsjfdjbfckd'
# s2 = 'fdjb'
# print(s1.find(s2))

"""
习题16：在字典中查找年龄最大的人，并输出
"""
# dict1 = {'bob': 18, 'alice': 20, 'mike': 48}
# age_name = sorted(zip(dict1.values(), dict1.keys()))
# age_max = max(age_name)
# age_min = min(age_name)
# print(age_name)
# print(age_max)
# print(age_min)

"""
习题17：列表转换为字典
"""
# k = ['bob', 'mike']
# v = [123, 456]
# print(dict(zip(k, v)))

"""
习题18：键盘输入一个字符串，将字符串中的小写字母变成大写，并输出到一个test.txt文件保存
"""
# f = open('test.txt', 'w')
# s = input('请输入一个字符串：')
# f.write(s.upper())
# f.close()
#
# f = open('test.txt', 'r')
# print(f.read())
# f.close()