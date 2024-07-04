from random import randint 
import matplotlib.pyplot as plt
from plotly.graph_objs import Bar,Layout
from plotly import offline

#创建骰子类
class Die:
    def __init__(self,num_sides = 6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1,self.num_sides)
#创建骰子的实例对象
die_1=Die()
die_2=Die(10)
a = die_1.roll()

#得到骰子投掷1000次的结果
'''results = []
for _ in range(50_000):
    result = die_1.roll()+die_2.roll()
    results.append(result)'''
#使用列表解析
results = [die_1.roll()+die_2.roll() for result in range(50_000)]

# print(results)
# print(len(results))

x = range(1,1001)
y = results

frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
'''for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)'''
#使用列表解析
frequencies = [results.count(value) for value in range(2,max_result+1) ]



#绘制1000次投掷结果的直方图
x_values = list(range(2,max_result+1))
data = [Bar(x = x_values,y=frequencies)]
x_axis_config = {'title':'结果','dtick':1}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title = '掷一个D6 和一个D10 50 000次的结果',xaxis = x_axis_config,yaxis = y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6_d10.html')


