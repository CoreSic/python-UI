from tkinter import *


root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT,fill=Y) # 需要先 将滚动条放置 到一个合适的位置 , 然后开始填充 . 

lb = Listbox(root,yscrollcommand=sb.set) # 内容 控制滚动条 . 

for i in range(111):
    lb.insert(END,i)
 
lb.pack(side=LEFT,fill=BOTH)

sb.config(command=lb.yview)  # 滑轮控制内容 . 

mainloop()