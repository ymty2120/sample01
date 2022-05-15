#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.state('zoomed')
root.geometry('1200x1600')

# キャンバスを作成
canvas = tkinter.Canvas(root, height=1200, width=1600)

#縦線
canvas.create_line(925, 80, 925, 720)
canvas.create_line(700, 80, 700, 720)

#横線
canvas.create_line(450, 277, 1150, 277)
canvas.create_line(450, 514, 1150, 514)

#〇
#1列目
canvas.create_oval(500, 250, 650, 100)
canvas.create_oval(740, 250, 890, 100)
canvas.create_oval(970, 250, 1120, 100)
#2列目
canvas.create_oval(500, 320, 650, 470)
canvas.create_oval(740, 320, 890, 470)
canvas.create_oval(970, 320, 1120, 470)
#3列目
canvas.create_oval(500, 550, 650, 700)
canvas.create_oval(740, 550, 890, 700)
canvas.create_oval(970, 550, 1120, 700)

#×
#1列目
canvas.create_line(500, 250, 650, 100, fill='red')
canvas.create_line(650, 250, 500, 100, fill='red')
canvas.create_line(740, 250, 890, 100, fill='red')
canvas.create_line(890, 250, 740, 100, fill='red')
canvas.create_line(970, 250, 1120, 100, fill='red')
canvas.create_line(1120, 250, 970, 100, fill='red')
#2列目
canvas.create_line(500, 320, 650, 470, fill='red')
canvas.create_line(650, 320, 500, 470, fill='red')
canvas.create_line(740, 320, 890, 470, fill='red')
canvas.create_line(890, 320, 740, 470, fill='red')
canvas.create_line(970, 320, 1120, 470, fill='red')
canvas.create_line(1120, 320, 970, 470, fill='red')
#3列目
canvas.create_line(500, 550, 650, 700, fill='red')
canvas.create_line(650, 550, 500, 700, fill='red')
canvas.create_line(740, 550, 890, 700, fill='red')
canvas.create_line(890, 550, 740, 700, fill='red')
canvas.create_line(970, 550, 1120, 700, fill='red')
canvas.create_line(1120, 550, 970, 700, fill='red')

# キャンパスを描画
canvas.pack()

# ウィンドウのループ処理
root.mainloop()


# In[ ]:




