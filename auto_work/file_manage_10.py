import shutil,os
from pathlib import Path
#复制文件和文件夹
p = Path.cwd()
# shutil.copy(p/'file_wr_9.py',p/'file_test.py')

#文件和文件夹的移动以及重命名
shutil.move(p/'a.txt',p/'..'/'b.txt')

#永久删除文件和文件夹




