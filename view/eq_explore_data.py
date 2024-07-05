import json
#探索数据的结构
filename = 'data/eq_data_1_day_m1.json'
with open (filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open (readable_file,'w') as f_1:
    json.dump(all_eq_data,f_1,indent=4)

#提取和features的键值以得到统计地震的次数
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

#提取震级
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
#提取位置数据

#绘制震级散点图
