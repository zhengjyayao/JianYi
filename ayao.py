# coding:utf-8
import requests
from bs4 import BeautifulSoup

def getHtml(url):
    res = requests.get(url)
    return res

rest = getHtml("https://movie.douban.com/subject/26752088/comments?sort=new_score&status=P")
html = rest.text
rest.encoding = 'utf-8' #设置编码类型
soup = BeautifulSoup(html,'html.parser')
total = soup.select('.comment-item') #选择爬取的类
##循环输出
for item in total:
    author =  item.select('.comment-info')
    items = author[0].select('a')
    con = item.select('.short')
    print(items[0].text, con[0].text)

