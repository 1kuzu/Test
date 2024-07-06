import requests

#处理API响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#处理响应字典
response_dict = r.json()
#指出目前GitHub总共包含了多少个仓库
print(f"Total repositories:{response_dict['total_count']}")

#探索有关仓库的信息
repo_dicts = response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")

#研究第一个仓库
# repo_dict=repo_dicts[0]
# print(f"\nkeys:{len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

print("提取一些关于仓库的信息")
for repo_dict in repo_dicts:
    print(f"项目的名称：{repo_dict['name']}")
    print(f"所有者：{repo_dict['owner']['login']}")
    print(f"获得的星数：{repo_dict['stargazers_count']}")
    print(f"仓库地址网页地址：{repo_dict['html_url']}")
    print(f"创建的时间：{repo_dict['created_at']}")
    print(f"最后的更新时间：{repo_dict['updated_at']}")
    print(f"关于项目的介绍：{repo_dict['description']}\n")







