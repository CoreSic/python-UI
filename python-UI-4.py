from tkinter import *

root = Tk()

s1 = Scale(root,from_=-10,to=10,tickinterval=5,resolution=2,length=100) # tickinterval 是设置的 标尺 多少长度有一个可读 , resolution设置的是 一次跳跃的 长度 . length 是设置长度 . 
s1.pack()
s2 = Scale(root,from_=-100,to=100,orient=HORIZONTAL,tickinterval=5,length=400,resolution=2)  # roient 默认的是 x 轴  , 让roient = HORIZONTAL 设置Y 轴 尺度 . 
s2.pack()

def Location_show():
    print('X轴位置 :'+str(s1.get()))
    print('Y轴位置 :'+str(s2.get()))
    
Button(root,text='获取位置',command=Location_show).pack()

mainloop()