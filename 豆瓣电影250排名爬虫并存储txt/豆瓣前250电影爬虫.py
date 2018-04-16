import requests
from bs4 import BeautifulSoup
def get_movies():
	headers = {'user-agent':"Mozilla/5.0 (Windows NT 6.1;Win64; x64)ApplewebKit/537.36(KHTML,like Gecko) Chrome/52.0.2743.82 Safari/537.36",'Host':"movie.douban.com"}
	movie_list=[]
	for i in range(0,10):
		link = "https://movie.douban.com/top250?start="+str(i*25)
		r = requests.get(link,headers=headers,timeout=10)
		print(str(i+1),"页面状态码:",r.status_code)
		soup = BeautifulSoup(r.text,'lxml')
		div_list = soup.find_all('div',class_= 'hd')
		for each in div_list:
			movie = each.a.span.text.strip()
			movie_list.append(movie)
	return movie_list
movies = get_movies()
str_movies=str(movies)
with open("电影.txt","a+") as f:
	f.write(str_movies)
	f.close()
