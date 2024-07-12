import webbrowser
import requests
import bs4
#使用webbrowser模块打开网站
# webbrowser.open('https://www.baidu.com')
#用requests下载一个网页
website_0 = requests.get('https://www.baidu.com')
print(type(website_0))
print(website_0.status_code == requests.codes.ok) 
print(len(website_0.text))
print(website_0.text[:250])

#检查是否连接成功
website_0.raise_for_status()

#将下载的网页写入文件当中,'wb'表示的是二进制方式
with open('website_baidu.html','wb') as f:
    for _ in website_0.iter_content(250):
        f.write(_)

