from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
from tkinter import Listbox
def douban():
	html = "https://movie.douban.com/top250?start="
	for i in range(0,10):
		url = html+str(i*25)
		r = requests.get(url,timeout=10)
		soup = BeautifulSoup(r.text,"html.parser")
		title = soup.find_all("div",class_="hd")
		for each in title:
			content = each.a.span.text
			list_box.insert(END,content)
			

root = Tk()#创建窗口
root.title("豆瓣排名前250的电影在这里!")
root.geometry('+500+250')


Label(root,text='欢迎您的到来!').grid(row=0,column=0)

hite_but = Button(root,text="点击我获得电影!",command=douban)
hite_but.grid(row=0,column=1)
list_box = Listbox(root,width = 30)
list_box.grid(row=1,columnspan=2)

root.mainloop()