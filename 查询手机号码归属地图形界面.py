import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
from tkinter import Listbox
#后台代码用来查询电话号码的信息
def phone_info():
	table_info = []
	url = 'http://www.ip138.com:8080/search.asp?mobile='+ent_search.get()+'&action=mobile'
	r = requests.get(url,timeout=30)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	soup = BeautifulSoup(r.text,'html.parser')
	table = soup.find_all('td')
	for each in table:
		table_info.append(each.text)
	a1="**查询成功**"
	a2="号码归属地:"
	a3=table_info[6]
	a4="卡类型:"
	a5=table_info[8]
	a6="区号:"
	a7=table_info[-3]
	a8="邮编:"
	mail_num = table_info[-1]
	a9=mail_num[:7]

	list_box.insert(END,a1)
	list_box.insert(END,a2)
	list_box.insert(END,a3)
	list_box.insert(END,a4)
	list_box.insert(END,a5)
	list_box.insert(END,a6)
	list_box.insert(END,a7)
	list_box.insert(END,a8)
	list_box.insert(END,a9)
#界面代码


root = Tk()
root.title("电话号码查询")
root.geometry("+600+350")
Label(root,text="请输入要查询的电话号码:").grid(row = 0,column = 0)
ent_search = Entry(root)
ent_search.grid(row = 0,column=1)
btn_search = Button(root,text='点击查询',command=phone_info)
btn_search.grid(row = 0,column = 2)
list_box = Listbox(root,width=60)
list_box.grid(row = 1,columnspan=3)
root.mainloop()
		

	