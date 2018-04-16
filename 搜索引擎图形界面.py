from tkinter import *
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
def search():
	word_key = en1.get()
	link = 'http://www.baike.com/wiki/'
	r = requests.get(link+str(word_key),timeout=20)
	r.encoding = r.apparent_encoding
	soup = BeautifulSoup(r.text,'html.parser')
	content = soup.find('div',class_='summary')
	list_box.insert(END,content.p.text)
#图形界面分割线
root =Tk()
root.title('影搜')
root.geometry('+600+350')
Label(root,text="请输入要搜索的关键词:").grid(row = 0, column = 0)
en1 = Entry(root)
en1.grid(row = 0,column = 1)
bn1 = Button(root,text = '搜索..',command = search)
bn1.grid(row = 0, column = 2)
list_box = Text(root,width = 50,height = 20)
list_box.grid(row = 5,columnspan = 3)

root.mainloop()