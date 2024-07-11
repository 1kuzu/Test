from operator import itemgetter
import requests
import json

#执行API调用并存储响应
url ='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print(f"Status code:{r.status_code}")
# response_dict = r.json()
# readable_file = "data/readable_hn_data.json"
# with open(readable_file,'w') as f:
#     json.dump(response_dict,f,indent=4)

#处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id:{submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()
    try:
        submission_dict = {
            'title':response_dict['title'],
            'hn_link':f"http://news.yconbinator.com/item?id={submission_id}",
            'comments':response_dict['descendants'], 
        }
    except KeyError:
        pass
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),
    reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle:{submission_dict['title']}")
    print(f"Discussion link:{submission_dict['hn_link']}")
    print(f"Comments:{submission_dict['comments']}")
    



