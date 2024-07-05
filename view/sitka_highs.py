import csv
import matplotlib.pyplot as plt
from datetime import datetime

#打开CSV文件并且读取表头
filename = 'data/sitka_weather_2018_simple.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #打印表头和它的位置
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    # 提取并且读取数据
    dates,highs,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        


    #列表解析的形式
    #reader读取文件过后将会关闭文件，所以需要先提取数据写入列表
    '''yet_read =[]
    for line in reader:
        yet_read.append(line)
    dates = [datetime.strptime(_[2],'%Y-%m-%d') for _ in yet_read]
    highs = [int(_[5]) for _ in yet_read]
    print(highs)
    print(dates)'''

#根据最高温度绘制图形
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red')
ax.plot(dates,lows,c='blue')
#填充两个Y值之间的空间，alpha表示的是透明度，facecolor是填充颜色
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#设置图形的格式
ax.set_title('Daily highests degree',fontsize = 24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('degree',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()

# first_date =datetime.strptime('2018-07-01','%Y-%m-%d')
# print(first_date)

