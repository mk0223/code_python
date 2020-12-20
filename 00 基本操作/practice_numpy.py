import numpy as np

"""
习题1：打印当前Numpy版本
"""
# print(np.__version__)

"""
习题2：构造一个全零的矩阵，并打印其占用的内存大小
"""
# a = np.zeros((3, 3))
# print('{} bytes'.format(a.size *a.itemsize))

"""
习题3：打印一个函数的帮助文档，比如numpy.add
"""
# print(help(np.info(np.add)))

"""
习题4：创建一个10-49的数组，并将其倒序排列
"""
# a = np.arange(10,50,1)
# # a = sorted(a, reverse=1)
# a = a[::-1]
# print(a)

"""
习题5：找到一个数组中不为0的索引
"""
# a = np.nonzero([1,2,0,3,0,0,5])
# print(a)

"""
习题6：随机构造一个3*3矩阵，并打印最大值和最小值
"""
# a = np.random.randint(0, 10, size=(3, 3))
# print(a)
# print('a.max =', a.max())
# print('a.min =', a.min())

"""
习题7：构造一个5*5的矩阵，令其值都为1，并在最外层加上一圈0
"""
# a = np.ones((5,5), dtype=int)
# a = np.pad(a, pad_width=1, mode='constant', constant_values=0)
# print(a)

"""
习题8：构件一个shape为（6，7，8）的矩阵，并找到第100个元素的索引值
"""
# a = np.random.random((6,7,8))
# a100 = np.unravel_index(100, (6,7,8))
# print(a100)

"""
习题9：对一个5*5的矩阵做归一化操作
"""
# a = np.random.random((5,5))
# a_max = a.max()
# a_min = a.min()
# a = (a - a_min)/(a_max - a_min)
# print(a)

"""
习题10：找到两个数组中相同的值
"""
# a = np.random.randint(0, 10, (3, 3))
# b = np.random.randint(0, 10, (3, 3))
# print(a)
# print(b)
# print(np.intersect1d(a, b))

"""
习题11：得到今天，明天，昨天的日期
"""
# yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
# today = np.datetime64('today', 'D')
# tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
# print(yesterday)
# print(today)
# print(tomorrow)

"""
习题12：得到一个月所有的天
"""
# date = np.arange('2020-11', '2020-12', dtype='datetime64[D]')
# print(date)

"""
习题13：得到一个数的整数部分
"""
# a = np.random.random((3,3)) * 10             #随机生成一个float数组
# a1 = np.random.randint(1, 10, size=(3,3))    #随机生成一个int数组，不包含最大值
# a2 = np.random.uniform(1, 10, size=(3,3))    #随机生成一个float数组，不包含最大值
# print(a)
# print(a1)
# print(a2)
# b = np.floor(a)     #向下取整
# print(b)
# c = np.trunc(a)     #截取整数
# print(c)
# d = np.ceil(a)      #向上取整
# print(d)
# e = np.round(a, 2)  #保留几位小数
# print(e)

"""
习题14：构造一个数组，让它不能被改变
"""
# a = np.zeros(5)
# print(a)
# a.flags.writeable = False
# a[0] = 1
# print(a)

"""
习题15：打印大数据的部分值，全部值
"""
# np.set_printoptions(threshold=5)         #限制打印出来一部分
# np.set_printoptions(threshold=np.nan)    #限制全部打印出来
# a = np.zeros((10, 10))
# print(a)

"""
习题16：找到在一个数组中，最接近一个数的索引
"""
# np.set_printoptions(threshold=5)
# a = np.arange(100)             #生成一个0-100（不包含100）的随机数组
# v = np.random.uniform(0,100)   #生成一个0-100（不包含100）的随机数
# print(v)
# index = (np.abs(a-v)).argmin() #找到相减后绝对值最小的那个数的index
# print(a[index])

"""
习题17：32位float类型和32位int类型转换
"""
# a = np.arange(10, dtype=np.float32)
# print(a.dtype)
# print('10个float类型数组共占{}bytes'.format(a.size * a.itemsize))
# b = a.astype(np.int32)      #转换元素类型
# print(b.dtype)
# print('10个int类型数组共占{}bytes'.format(b.size * b.itemsize))

"""
习题19：打印数组元素位置坐标与数值
"""
# a = np.arange(9).reshape((3,3))
# for index, value in np.ndenumerate(a):   #枚举遍历元素值和位置Index
#     print(index, value)

"""
习题20：按照数组的某一列进行排序
"""
# a = np.random.randint(0, 10, size=(3, 3))
# print(a)
# b = a[a[:, 1].argsort()]
# print(b)

"""
习题21：统计数组中每个数值出现的次数
"""
# a = np.random.randint(1, 10, size=(4, 4))
# print('a =\n', a)
# a = np.ravel(a)        #把数组展平后才能进行np.bincount()操作
# b = np.bincount(a)     #从0到最大值出现的次数统计
# print(b)
# for i in range(np.max(a)+1):
#     print('在数组a中，{}出现的次数是{}'.format(i, b[i]))

"""
习题22：如何对一个四维数组的最后两维来求和
"""
# a = np.random.randint(0, 10, size=(4, 4, 4, 4))
# res = a.sum(axis=(-2, -1))  #按照那个维度求和就把哪个维度的轴写上去
# print(res)

"""
习题23：交换矩阵中的两行
"""
# a = np.arange(9).reshape((3, 3))
# print(a)
# a[[0, 1, 2], :] = a[[1, 0, 2], :]   #交换一个数组中的两行
# print(a)
# a[:, [0, 1, 2]] = a[:, [1, 0, 2]]   #交换一个数组中的两列
# print(a)

"""
习题24：统计数组中每个数值出现的次数
"""
# a = np.random.randint(1, 10, size=(4, 4))
# print('a =\n', a)
# a = np.ravel(a)        #把数组展平后才能进行np.bincount()操作
# b = np.bincount(a)     #从0到最大值出现的次数统计
# print(b)
# print('数组a中最常出现的数字是{}，一共出现了{}次。'.format(b.argmax(), b.max()))

"""
习题25：快速查找TOP K
"""
# a = np.arange(1000)
# n = 5
# np.random.shuffle(a)
# print(a[np.argpartition(a, -n)[-n:]])     #查找TOP K的数, a是要查找的数组，n是第n大的数字放在第n个位置，前面的都小于这个数，后面的都大于这个数。

"""
习题26：去掉一个数组中所有元素都相同的数据行
"""
a = np.random.randint(0, 2, (10, 3))
print(a)
e = np.all(a[:, 1:] == a[:, :-1], axis=1)
print(e)

b = np.delete(a, a[i for i in range(10) if e[i]])

