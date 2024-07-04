import csv
import matplotlib.pyplot as plt
from datetime import datetime

#打开CSV文件并且读取表头
filename = 'sitka_weather_07-2018_simple.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #打印表头和它的位置
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    # 提取并且读取数据
    highs = [int(row[5]) for row in reader]
    print(highs)

#根据最高温度绘制图形
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(highs,c='red')

#设置图形的格式
ax.set_title('The highest degree',fontsize = 24)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel('degree',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()
