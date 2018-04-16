from tkinter import *
import requests
from bs4 import BeautifulSoup
from tkinter.messagebox import *
def get_img(img_name):
	roo = Tk()
	roo.title(img_name)
	img = PhotoImage(file = img_name)	
	label1 = Label(root,image = img)
	label1.grid(row = 1, columnspan =3)
	roo.mainloop() 

def get_name():
	name = ent1.get()
	url = 'http://www.uustv.com/'
	data = {'fontcolor':'#000000',
	'fonts':'jfcs.ttf',
	'sizes':'60',
	'word':str(name)}
	r = requests.post(url,data=data)
	r.encoding = r.apparent_encoding 
	print(r.status_code)
	soup = BeautifulSoup(r.text,'html.parser')
	div = soup.find('div',class_='tu')
	img_url = url+div.img['src']
	img_url_get = requests.get(img_url)
	img_name = name+'.gif'
	with open(img_name,'wb') as f:
		f.write(img_url_get.content)
	get_img(img_name)
root = Tk()
root.title('签名设计')
root.geometry('+600+350')
Label(root,text='请输入您的姓名:').grid(row = 0,column = 0)
ent1 = Entry(root)
ent1.grid(row = 0,column = 1)
img0 = PhotoImage(file = '未闻花名.gif')
label_img = Label(root,image=img0)
label_img.grid(row = 1,columnspan= 3)
btn1 = Button(root,text = '设计',command=get_name)
btn1.grid(row = 0,column = 2)


root.mainloop()
	
	