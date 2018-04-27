from tkinter import *
root = Tk()
root.title('云音')
root.geometry('700x500+600+250')
frame_list = Frame(root,width = 200,height = 450,bg='#DCDCDC',borderwidth=2)
frame_list.grid(rowspan = 2, column = 0)

frame_information = LabelFrame(root,width = 500, height = 150,bg="#C0C0C0",text = '歌单')
frame_information.grid(row = 0, column = 1)

frame_main = Frame(root,width = 500, height = 300,bg="#F08080",borderwidth=2)
frame_main.grid(row = 1, column = 1)

frame_bottom = Frame(root,width = 700,height = 50,bg = "#40E0D0",borderwidth=2)
frame_bottom.grid(row = 2,columnspan = 2)

button_search = Button(frame_list,text = '搜索',width = 20)
button_search.grid(row = 0,column = 0)

button_find = Button(frame_list,text = '发现音乐',width = 20)
button_find.grid(row = 1,column = 0)

button_MV = Button(frame_list,text = 'MV',width = 20)
button_MV.grid(row = 2,column = 0)

button_friend = Button(frame_list,text = '朋友',width = 20)
button_friend.grid(row = 3,column = 0)

button_search = Button(frame_list,text = '搜索',width = 20)
button_search.grid(row = 4,column = 0)

Label_mymusic = Label(frame_list,text = '我的音乐',width = 20,fg = 'blue')
Label_mymusic.grid(row = 5,column = 0)

button_localhost = Button(frame_list,text = '本地音乐',width = 20)
button_localhost.grid(row = 6,column = 0)

button_download= Button(frame_list,text = '下载管理',width = 20)
button_download.grid(row = 7,column = 0)
#下端图片
photo_back = PhotoImage(file = '后退.png')
img_back = Label(frame_bottom,imag = photo_back)
img_back.grid(row = 0 ,column = 0,pady = 8)

photo_stop = PhotoImage(file = '暂停.png')
img_stop = Label(frame_bottom,imag = photo_stop)
img_stop.grid(row = 0 ,column = 2,pady = 8)

photo_quick = PhotoImage(file = '快进.png')
img_quick = Label(frame_bottom,imag = photo_quick)
img_quick.grid(row = 0 ,column = 3,pady = 8,sticky='E')
root.mainloop()