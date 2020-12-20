"""
数据特征简介
•datetime - 每小时日期+时间戳
•season - 1 =春天，2 =夏天，3 =秋天，4 =冬天
•holiday - 这一天是否被视为假日
•workingday - 这一天既不是周末也不是假日
•weather -
    ◾1: 晴，少云，部分多云，部分多云。
    ◾2: 雾+云，雾+碎云，雾+少云，雾
    ◾3: 小雪，小雨+雷雨+散云，小雨+散云
    ◾4: 大雨+冰盘+雷雨+雾，雪+雾
•temp - 温度摄氏
•atemp - “感觉”摄氏温度
•humidity - 相对湿度
•windspeed - 风的速度
•casual - 发起非注册用户租金的数目
•registered - 发起注册用户租金的数目
•count - 租金总额（因变量）
"""

#（一）:导入所需python工具库
import pylab
import calendar
import numpy as np
import pandas as pd
import seaborn as sns
import missingno as msno
from scipy import stats
from datetime import datetime
import matplotlib.pyplot as plt
import warnings
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore", category=DeprecationWarning)

#（二）：使用Pandas读取数据，并观察数据的维度以及特征的类型
dailyData = pd.read_csv("train.csv")

# 数据集的大小
print(dailyData.shape)

# 通过打印几行数据来了解数据
# 最大显示列为20列
pd.set_option('display.max_columns', 20)
print(dailyData.head(2))

# 什么类型的变量在我们的数据中？
print(dailyData.dtypes)

# （三）：特征组合：

# datetime列提取出日期
dailyData["date"] = dailyData.datetime.apply(lambda x : x.split()[0])
# print(dailyData['date'].head(2))

# datetime列提取出几点
dailyData["hour"] = dailyData.datetime.apply(lambda x : x.split()[1].split(":")[0])
# print(dailyData['hour'].head(2))

# datetime列提取出几分
dailyData["minute"] = dailyData.datetime.apply(lambda x : x.split()[1].split(":")[1])
# print(dailyData['minute'].head(2))

# datetime列提取出几秒
dailyData["second"] = dailyData.datetime.apply(lambda x : x.split()[1].split(":")[2])
# print(dailyData['second'].head(2))

# datetime列提取出周几
dailyData["weekday"] = dailyData.date.apply(lambda dateString : calendar.day_name[datetime.strptime(dateString,"%Y-%m-%d").weekday()])
# print(dailyData['weekday'].head(2))

# datetime列提取出几月份
dailyData["month"] = dailyData.date.apply(lambda dateString : calendar.month_name[datetime.strptime(dateString,"%Y-%m-%d").month])
# print(dailyData['month'].head(2))

# 根据season列对应找出季节
dailyData["season"] = dailyData.season.map({1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"})
# print(dailyData['season'].head(2))

# 根据weather列对应找出天气
dailyData["weather"] = dailyData.weather.map({1: " Clear + Few clouds + Partly cloudy + Partly cloudy",\
                                        2 : " Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist ", \
                                        3 : " Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", \
                                        4 :" Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog " })
# 设置单元格显示最大宽度为100
pd.set_option('display.max_colwidth', 100)
# print(dailyData['weather'].head(2))

# 去掉datetime这列
dailyData = dailyData.drop(["datetime"], axis=1)
# print(dailyData.head(2))

# 将种类型变量定义成category类型
# print(dailyData.dtypes)
categoryVariableList = ["hour", "weekday", "month", "season", "weather", "holiday", "workingday"]
for var in categoryVariableList:
    dailyData[var] = dailyData[var].astype("category")
print(dailyData.dtypes)

# （三）：构造变量类型的dataframe并画图展示

# 计算不同类型的变量个数（category，int,float,object）
dataTypeDf = pd.DataFrame(dailyData.dtypes.value_counts()).reset_index().rename(columns={"index": "variableType", 0: "count"})

#要重新写入文件并读取一遍，否则报错”data type '' not understood“，原因未知？？
dataTypeDf.to_csv('dataTypeDf_c.csv')
dataTypeDf_c = pd.read_csv('dataTypeDf_c.csv')

# 使用seaborn的barplot进行画图展示
fig, ax = plt.subplots()
fig.set_size_inches(12, 5)
sns.barplot(data=dataTypeDf_c, x="variableType", y="count", ax=ax)
ax.set(xlabel='variable Typeariable Type', ylabel='Count', title="Variables DataType Count")
# 默认调整子图之间的距离
# plt.subplots_adjust(wspace=1, hspace=1)
# plt.tight_layout()
# plt.show()

#（四）使用Python工具进行缺失值展示
msno.matrix(dailyData, figsize=(6, 4))
# plt.show()

# （五）：观察利群点情况
# 使用boxplot绘制单变量图
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(8, 6)
sns.boxplot(data=dailyData, y="count", orient="v", ax=axes[0][0])
sns.boxplot(data=dailyData, y="count", x="season", orient="v", ax=axes[0][1])
sns.boxplot(data=dailyData, y="count", x="hour", orient="v", ax=axes[1][0])
sns.boxplot(data=dailyData, y="count", x="workingday", orient="v", ax=axes[1][1])
# 添加X轴与Y轴名称
axes[0][0].set(ylabel='Count', title="Box Plot On Count")
axes[0][1].set(xlabel='Season', ylabel='Count', title="Box Plot On Count Across Season")
axes[1][0].set(xlabel='Hour Of The Day', ylabel='Count', title="Box Plot On Count Across Hour Of The Day")
axes[1][1].set(xlabel='Working Day', ylabel='Count',title="Box Plot On Count Across Working Day")
# 默认调整子图之间的距离
# plt.subplots_adjust(wspace=1, hspace=1)
plt.tight_layout()
# 分析离群点分布，在原始数据中去掉你认为的离群点
dailyDataWithoutOutliers = dailyData[np.abs(dailyData["count"]-dailyData["count"].mean())<=(3*dailyData["count"].std())]
print ("Shape Of The Before Ouliers: ",dailyData.shape)
print ("Shape Of The After Ouliers: ",dailyDataWithoutOutliers.shape)
# 去掉离群点后绘制示意图
# 使用boxplot绘制单变量图
fig, axes = plt.subplots(nrows=2, ncols=2)
# 默认调整子图之间的距离
# plt.tight_layout()
fig.set_size_inches(8, 6)
sns.boxplot(data=dailyDataWithoutOutliers, y="count", orient="v", ax=axes[0][0])
sns.boxplot(data=dailyDataWithoutOutliers, y="count", x="season", orient="v", ax=axes[0][1])
sns.boxplot(data=dailyDataWithoutOutliers, y="count", x="hour", orient="v", ax=axes[1][0])
sns.boxplot(data=dailyDataWithoutOutliers, y="count", x="workingday", orient="v", ax=axes[1][1])
# 添加X轴与Y轴名称
axes[0][0].set(ylabel='Count', title="Box Plot On Count - A")
axes[0][1].set(xlabel='Season', ylabel='Count', title="Box Plot On Count Across Season - A")
axes[1][0].set(xlabel='Hour Of The Day', ylabel='Count', title="Box Plot On Count Across Hour Of The Day - A")
axes[1][1].set(xlabel='Working Day', ylabel='Count',title="Box Plot On Count Across Working Day - A")
# 默认调整子图之间的距离
# plt.subplots_adjust(wspace=1, hspace=1)
plt.tight_layout()
# plt.show()

# （六）：计算变量间相关系数
# 选择指定变量（"temp","atemp","casual","registered","humidity","windspeed","count"）
# 使用pandas的.corr()函数计算相关系数
corrMatt = dailyData[["temp", "atemp", "casual", "registered", "humidity", "windspeed", "count"]].corr()
mask = np.array(corrMatt)
mask[np.tril_indices_from(mask)] = False
# 使用seaborn的heatmap进行绘制
fig, ax = plt.subplots()
fig.set_size_inches(20, 10)
sns.heatmap(corrMatt, mask=mask, vmax=.8, square=True, annot=True)
# plt.show()
# 使用seaborn的regplot绘制变量回归图
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3)
fig.set_size_inches(12, 5)
sns.regplot(x="temp", y="count", data=dailyData, ax=ax1)
sns.regplot(x="windspeed", y="count", data=dailyData, ax=ax2)
sns.regplot(x="humidity", y="count", data=dailyData, ax=ax3)
# 默认调整子图之间的距离
# plt.subplots_adjust(wspace=1, hspace=1)
plt.tight_layout()

# （七）：统计count数量随月份，时间等因素变化的情况并绘图展示
# 使用groupby进行计算
# 使用seaborn进行绘图展示
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4)
fig.set_size_inches(6, 8)

sortOrder = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
hueOrder = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

monthAggregated = pd.DataFrame(dailyData.groupby("month")["count"].mean()).reset_index()
monthSorted = monthAggregated.sort_values(by="count", ascending=False)
sns.barplot(data=monthSorted, x="month", y="count", ax=ax1, order=sortOrder)
ax1.set(xlabel='Month', ylabel='Avearage Count', title="Average Count By Month")

hourAggregated = pd.DataFrame(dailyData.groupby(["hour", "season"], sort=True)["count"].mean()).reset_index()
sns.pointplot(x=hourAggregated["hour"], y=hourAggregated["count"], hue=hourAggregated["season"], data=hourAggregated, join=True, ax=ax2)
ax2.set(xlabel='Hour Of The Day', ylabel='Users Count', title="Average Users Count By Hour Of The Day Across Season", label='big')

hourAggregated = pd.DataFrame(dailyData.groupby(["hour", "weekday"], sort=True)["count"].mean()).reset_index()
sns.pointplot(x=hourAggregated["hour"], y=hourAggregated["count"], hue=hourAggregated["weekday"], hue_order=hueOrder, data=hourAggregated, join=True, ax=ax3)
ax3.set(xlabel='Hour Of The Day', ylabel='Users Count', title="Average Users Count By Hour Of The Day Across Weekdays", label='big')

hourTransformed = pd.melt(dailyData[["hour", "casual", "registered"]], id_vars=['hour'], value_vars=['casual', 'registered'])
hourAggregated = pd.DataFrame(hourTransformed.groupby(["hour", "variable"], sort=True)["value"].mean()).reset_index()
sns.pointplot(x=hourAggregated["hour"], y=hourAggregated["value"], hue=hourAggregated["variable"], hue_order=["casual", "registered"], data=hourAggregated, join=True, ax=ax4)
ax4.set(xlabel='Hour Of The Day', ylabel='Users Count', title="Average Users Count By Hour Of The Day Across User Type", label='big')
# 默认调整子图之间的距离
# plt.subplots_adjust(wspace=1, hspace=1)
plt.tight_layout()
plt.legend(loc='best')
plt.show()



