import shutil,os,send2trash,zipfile
from pathlib import Path

#复制文件和文件夹
p = Path.cwd()
# shutil.copy(p/'file_wr_9.py',p/'file_test.py')

# #文件和文件夹的移动以及重命名
# shutil.move(p/'a.txt',p/'..'/'b.txt')

#永久删除文件和文件夹
#删除单个文件的操作
# os.unlink(p/'a.txt')
#删除空文件夹的操作
# os.rmdir(p/'a')
#删除包含文件和文件夹的文件操作
# shutil.rmtree(p/'a')

#使用send2trash模块安全地删除文件和文件夹

# send2trash.send2trash('a')

#遍历目录树,分别返回当前的文件名，当前文件目录下的子文件夹，以及当前文件夹内的文件
# walk = os.walk(p/'..')
# for folder_name,subfolders,filename in walk:
#     print("当前的文件名称：",folder_name)
#     print(f"文件夹{folder_name}下的子文件夹:",subfolders)
#     print(f"文件夹{folder_name}下的文件:",filename,"\n")

#用zipfile压缩文件
#创建一个zipfile对象
exampleZip = zipfile.ZipFile(p/'cat.zip')
# print(exampleZip.namelist())
# spam = exampleZip.getinfo('cat.txt')
# #file_size是原文件大小，compress_size是压缩后的大小
# print(spam.file_size)
# print(spam.compress_size)

# #从zip文件中解压缩,使用extractall()方法
# exampleZip.extractall(p)
# exampleZip.close()

#从zip文件中解压单个文件使用extract()方法
# exampleZip.extract('cat.txt',p/'dog')
# exampleZip.close()

#创建和添加到ZIP文件
new_zip = zipfile.ZipFile('new.zip','w')
new_zip.write('cat.txt',compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()















