from tkinter import *

root = Tk()

text = Text(root ,width=50,height=10) # 这个意思是每行50个字符  10行 .

text.pack()

#第一个表示插入的位置第二个是内容其中第一个必须有，INSERT是光标所在位置.
text.insert(INSERT,"I Love github\n")
#END表示在上一次输入结束的位置继续. 
text.insert(END,"https://github.com/CoreSic/python-UI")  

mainloop()