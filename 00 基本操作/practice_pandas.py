import pandas as pd

# 显示所有列和行
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# 1. Pandas介绍
df = pd.read_csv('./data/train.csv')
#.head()可以读取前几条数据，指定前几条都可以
# print(df.head(6))
#.info返回当前的信息
# print(df.info())
# print(df.index)
# print(df.columns)
# print(df.dtypes)
# print(df.values)

# 2. Pandas基本操作
# 自己创建一个dataframe结构
# data = {'country': ['aaa', 'bbb', 'ccc'],
#         'population': [10, 12, 14]}
# df_data = pd.DataFrame(data)
# print(df_data)
# print(df_data.info())
# age = df['Age']
# print(age[:5])
# series: dataframe中的一行/列
# print(age.index)
# print(age.values[:5])