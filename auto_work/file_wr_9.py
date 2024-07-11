from pathlib import Path
import os

# path = Path('spam','bacon','eggs')

#用/连接路径
# path = Path('spam','bacon','eggs')/'high'/Path('sora')/Path('MING','HONG')
# print(path)

#当前的工作目录
# print(Path.cwd())
#主目录
# print(Path.home())
#用OS创建文件夹，可以一次嵌套多个目录
# os.makedirs('D:\\TONG\\MING')
#用Path来创建文件夹,一次只能创建一个目录
# Path(r'D:\python_study\ai').mkdir()

#返回当前路径的绝对路径的字符串
# print(os.path.abspath('.'))
# #判断当前路径是否是绝对路径
# print(Path.cwd().is_absolute())
# print(os.path.isabs(r'D:\python_study\auto_work'))
# #返回从开始路径到path路径的相对路径的字符串，如果没有就以当前目录作为开始路径
# print(os.path.relpath(r'D:\python_study',r'D:\python_study\auto_work'))

# #取得文件路径的各个部分
# p = Path(r'D:\python_study\auto_work\re_user_7.py')
# print(p.parent)
# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.drive)

# #用os获取文件路径的内容
# calcFilepath = r'C\jl\l\l'
# #获取最后一个斜杠后的内容
# print(os.path.basename(calcFilepath))
# #获取最后一个斜杠前的1所有内容
# print(os.path.dirname(calcFilepath))
# #获取一个包含路径名称和基本名称的元组
# print(os.path.split(calcFilepath))

#查看文件大小(返回字节数)
print(os.path.getsize(r'D:\python_study\auto_work\file_wr_9.py'))
#返回文件名字符串的列表
print(os.listdir(r'D:\python_study\auto_work'))
#使用通配符模式修改文件列表
p = Path(r'D:\python_study\auto_work')
print(list(p.glob('?????????.py')))

#检查路径的有效性
#检查路径是否存在
print(p.exists())
#检查路径是否存在并且是一个文件
print(p.is_file())
pf = p/'file_wr_9.py'
print(pf.is_file())
#检查是否是一个文件夹
print(p.is_dir())
#文件读写，跳过

#用shelve模块(二进制文件)保存变量
import shelve
# shelfFile = shelve.open('cat')
# cats = ['zlo','aja']
# shelfFile['cat_1'] = cats
# shelfFile.close()

# shelfFile = shelve.open('cat')
# print(type(shelfFile))
# shelfFile.close()

shelfFile =shelve.open('cat')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))

#用pprint.pformat()函数来保存变量,将列表，字典，函数等编码成文本形式的函数，可以使用文本编辑，加强了可编辑性和可复制可移植性。
import pprint
cats = {1:'add',2:'dffs','dfdsd':'sdcs'}
for _ ,_1 in cats.items():
    print(_,_1)
ppr = pprint.pformat(cats)
print(type(ppr))













