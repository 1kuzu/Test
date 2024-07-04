import matplotlib.pyplot as plt
from random_walk import RandomWalk
#绘制随机漫步的图表
while 1==1:
    rw = RandomWalk(5_000)
    rw.fill_walk()
    plt.style.use('seaborn')
    fig,ax = plt.subplots(figsize=(15,9),dpi=128)
    points_number = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=points_number,cmap=plt.cm.Blues,edgecolors='none',s=15)
    #突出起点和终点
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk?(y/n)')
    if keep_running =='n':
        break
