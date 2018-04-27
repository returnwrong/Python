import requests
from bs4 import BeautifulSoup

def music_top(link):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'}
	try:
		r = requests.get(link,timeout=20,headers=headers)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		print(r.status_code)
		return r.text
	except:
		print("获取音乐排名失败，请检查网络！")

# def music_soup(html):
# 	soup = BeautifulSoup(html,'html.parser')
# 	title = soup.find_all('div',class_="info")
# 	for each in title:
# 		print(each.text)
	
def main():
	title_=[]
	name_a_=[]
	link = 'http://www.xiami.com/chart/data?c=103&type=0&page=1&limit=100&_=1523093980034'
	date = music_top(link)
	soup = BeautifulSoup(date,'lxml')
	title = soup.find_all('div',class_='info')

	name_a = soup.find_all('a',class_='artist')
	z = 0
	for each in title:
		 title_.append(each.p.strong.a.text)
	for item in name_a:
		 name_a_.append(item.text)
	del name_a_[13]
	del name_a_[14]
	for (i,j) in zip(title_,name_a_):
		z+=1
		print('排名：',z)
		print('歌名：',i)
		print('演唱：',j)
		print()
		
		
if __name__ == '__main__':
	main()
