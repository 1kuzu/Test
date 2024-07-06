import json
import plotly.express as px
import pandas as pd
#探索数据的结构
filename = 'data/eq_data_30_day_m1.json'
with open (filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open (readable_file,'w') as f_1:
    json.dump(all_eq_data,f_1,indent=4)

#提取和features的键值以得到统计地震的次数
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

#提取震级，提取位置的数据
mags,titles,lons,lats=[],[],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    #添加进列表
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
    
print(mags[:10])
print(titles[:2])
print(lons[0:5])
print(lats[0:5])
#用pandas对数据列表进行了封装
data = pd.DataFrame(
    data = zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
)
data.head()
# print(type(data))

#绘制震级散点图
px.colors.qualitative.Alphabet
fig = px.scatter(
    # x=lons,
    # y=lats,
    # labels={'x':'经度','y':'纬度'},
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='GLOBAL EQ',
    size = '震级',
    size_max = 10,
    color='震级',
    #修改渐变色的配色方案
    color_continuous_scale='jet',
    hover_name='位置',
)
fig.write_html('global_earthquakes.html')
fig.show()
