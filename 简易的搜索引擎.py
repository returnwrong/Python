#简单的搜索引擎
from bs4 import BeautifulSoup
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0)Gecko/20100101 Firefox/57.0'}
key_word = input("请输入要搜索的关键字:")
url = "http://www.baike.com/wiki/"+str(key_word)
r = requests.get(url,timeout=10)
r.encoding = r.apparent_encoding
if r.status_code ==200:
	print("----------------------")
	print("内容获取成功!")
	print("----------------------")
	soup = BeautifulSoup(r.text,"html.parser")
	div_list = soup.find_all('div',class_="summary")
	for each in div_list:
		print(each.p.text)
else:
	print("内容获取失败!")
