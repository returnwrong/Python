import requests
from bs4 import BeautifulSoup
link = 'https://beijing.anjuke.com/sale/?from=navigation'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'}
try:
	r = requests.get(link,headers = headers,timeout = 20)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
except:
	print('获取失败！')

soup = BeautifulSoup(r.text,'lxml')

span_class =soup.find_all('span',class_='price-det')
price = []
for item in span_class:
	price.append(item.text)

houserListTitle = soup.find_all('div',class_='house-details')
num = -1
xv = 0
for each in houserListTitle:
	num+=1
	xv+=1
	print('排序：',xv)
	print('房屋信息：',each.contents[1].a.text.strip())
	print('户型:\t',each.contents[3].text.split('')[0])
	print('位置：',each.contents[5].text.strip())
	print('其他信息：',each.contents[7].text)
	print('价格：',price[num])
	print('---------------------------------------------------------------')
	
