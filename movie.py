import requests
from bs4 import BeautifulSoup
import json 

#url = "https://movie.douban.com/"
#soup = BeautifulSoup(requests.get(url).text, 'html.parser')


#con = []
#links = soup.select('.billboard-bd')

#for link in links:
#    items = link.find_all('a')
#    for item in items:
#        lists = []
#        li = item['href']
#        name = item.text
#        lists.append(li)
#        lists.append(name)
#        con.append(lists)

def getLink(url,cl):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    lists = soup.select(cl)
    con = []
    for list in lists:
        items = list.find_all('a')
        for item in items:
            links =[]
            link = item['href']
            movie = item.text
            links.append(link)
            links.append(movie)
            con.append(links)
    return con

def getCommer(url,cl):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    lists = soup.select(cl)
    con = []
    for list in lists:
        items = list.select('.comment')
        for item in items:
            content = []
            au = item.select('.comment-info')
            author = au[0].select('a')
            commer = item.select('.short')
            content.append(author[0].text)
            content.append(commer[0].text)
            con.append(content)
    return con


def getPraise(url,cl):
    PraiseList = []  ##豆瓣电影口碑榜
    WorkArea = []    ##数据存放区

    PraiseList = getLink(url,cl)
    for lists in PraiseList:
        url = lists[0]+"comments?sort=new_score&status=P"
        con = []
        con =  getCommer(url,'.comment-item')
        data = []
        data.append(lists[1])
        data.append(con)
        WorkArea.append(data)
    return WorkArea


Praise =  getPraise('https://movie.douban.com/','.billboard-bd')
#print(Praise)
data = {}
i = 1
for p in Praise:
    Parent  ={}
    reviews = p[1]
    Parent ['影片'] = p[0]
    #print(p[1])
    j = 1
    for review in reviews:
        children = {}
        children['作者'] = review[0]
        children['内容'] = review[1]
        Parent[j] = children
        j = j+1
    data[i] = Parent
    i = i+1
result = bytes(json.dumps(data,ensure_ascii=False), encoding = "utf8")  
with open('result.txt', 'wb') as f:
    f.write(result)