import requests
from plotly.graph_objs import Bar
from plotly import offline

import requests

#处理API响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#处理响应字典,处理结果
response_dict = r.json()
#指出目前GitHub总共包含了多少个仓库
# print(f"Total repositories:{response_dict['total_count']}")
#探索有关仓库的信息
repo_dicts = response_dict['items']
# print(f"Repositories returned:{len(repo_dicts)}")
repo_links,stars,labels=[],[],[]
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'> {repo_name} </a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br  />{description}"
    labels.append(label)

#可视化操作
data=[{'type':'bar',
       'x':repo_links,
       'y':stars,
       'hovertext':labels,
       'marker':{
                 'color':'rgb(60,100,150)',
                 'line':{'width':1.5,
                         'color':'rgb(25,25,25)'
                        },
                },
        'opacity':0.6,
      }]
        
my_layout ={
            'title':'Github上最受欢迎的项目',
            'titlefont':{'size':24},
            'xaxis':{'title':'项目名称',
                     'titlefont':{'size':24},
                     'tickfont':{'size':14}
                    },
            'yaxis':{'title':'获得的星数',
                     'titlefont':{'size':24},
                     'tickfont':{'size':14},
                    },
            }

fig ={'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')



#研究第一个仓库
# repo_dict=repo_dicts[0]
# print(f"\nkeys:{len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("提取一些关于仓库的信息")
# for repo_dict in repo_dicts:
#     print(f"项目的名称：{repo_dict['name']}")
#     print(f"所有者：{repo_dict['owner']['login']}")
#     print(f"获得的星数：{repo_dict['stargazers_count']}")
#     print(f"仓库地址网页地址：{repo_dict['html_url']}")
#     print(f"创建的时间：{repo_dict['created_at']}")
#     print(f"最后的更新时间：{repo_dict['updated_at']}")
#     print(f"关于项目的介绍：{repo_dict['description']}\n")