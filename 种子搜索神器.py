import requests
from bs4 import BeautifulSoup
seach_name = input("请输入你要搜索的资源名:")
for i in range(1,11):
	html = 'http://www.btrabbit.net/search/'+str(seach_name)+'/default-'+str(i)+'.html'
	r = requests.get(html,timeout=10)
	r.encoding = r.apparent_encoding
	soup = BeautifulSoup(r.text,"html.parser")
	div_all = soup.find_all('div',class_='search-item detail-width')

	for each in div_all:
		print("-------------------------------------------------------")
		print(each.get_text())
		for s in each.find_all('a'):
			print('###我是磁力链接请复制我:',s.get('href'))
			print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->")