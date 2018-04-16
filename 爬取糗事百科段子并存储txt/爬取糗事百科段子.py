'''
content:爬取糗事百科段子
author:T-Bone
date:2018.2.2

'''
#导入模块
import requests
from bs4 import BeautifulSoup
from tkinter import *


def htmlcontent(url):#获取网页源码
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0'}
	try:
		r = requests.get(url,timeout = 20,headers = headers)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
		
	except:
		print("段子获取失败,请检查网络!")
	
	
def html_soup(html):#解析网页源码获得段子
	soup = BeautifulSoup(html,'html.parser')
	div_content = soup.find_all('div',class_='content')
	s = range(1,101)
	for s,item in  zip(s,div_content):
		gui_list = '('+str(s)+')'+item.span.text.strip()
		print(gui_list)
		print('--------------------------------------------------------------------------------')
		'''
		with open('123.txt','a+') as f: #用于写入文件
			
			f.write(gui_list)
			f.write('\n')
			f.write('\n')
		'''

def main():#主函数
	for i in range(1,11):
		url = 'https://www.qiushibaike.com/text/page/'+str(i)
		html = htmlcontent(url)
		print('--------------------------------------------------------------------------------')
		html_soup(html)

	
	

	
main()

		

	