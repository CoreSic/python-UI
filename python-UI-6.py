from tkinter import *
import datetime

now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

root = Tk()

Label(root,text='帐号 :').grid(row=0,column=0) # 对Label内容进行 表格式 布局
Label(root,text='密码 :').grid(row=1,column=0)

v1=StringVar()    # 设置变量 . 
v2=StringVar()

e1 = Entry(root,textvariable=v1)            # 用于储存 输入的内容  
e2 = Entry(root,textvariable=v2,show='*')
e1.grid(row=0,column=1,padx=10,pady=5)      # 进行表格式布局 . 
e2.grid(row=1,column=1,padx=10,pady=5)
def show():
    print("帐号 :%s" % e1.get())          # get 变量内容 
    print("密码 :%s" % e2.get())

name=now_time
msg="12345"

# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create():
    desktop_path = "D:\\My_Resource\\class_program\\4.python\\临时文件\\"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)   #msg也就是下面的Hello world!
    # file.close()

Button(root,text='取消',width=10,command=root.quit).grid(row=3,column=0,sticky=W,padx=10,pady=5) 
# 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 . 
Button(root,text='确定',width=10,command=text_create).grid(row=3,column=1,sticky=E,padx=10,pady=5)  


mainloop()



 
