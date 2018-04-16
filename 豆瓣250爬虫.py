from bs4 import BeautifulSoup
movie_list=[]
import requests
html = "https://movie.douban.com/top250?start="
for i in range(0,10):
	url = html+str(i*25)
	r = requests.get(url,timeout=10)
	soup = BeautifulSoup(r.text,"html.parser")
	title = soup.find_all("div",class_="hd")
	for each in title:
		print(each.a.span.text)
	
		
	


