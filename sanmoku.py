#!/usr/bin/env python
# coding: utf-8

# In[18]:


import tkinter

#
# GUI設定
#
root = tkinter.Tk()
root.title('三目並べ')
root.state('zoomed')
root.geometry('1600x1200')

#
#〇描画
#
#１行目
def draw11(event):
    canvas.create_oval(500, 250, 650, 100, tag='〇×')

def draw12(event):
    canvas.create_oval(740, 250, 890, 100, tag='〇×')

def draw13(event):
    canvas.create_oval(970, 250, 1120, 100, tag='〇×')

#２行目
def draw21(event):
    canvas.create_oval(500, 320, 650, 470, tag='〇×')
    
def draw22(event):
    canvas.create_oval(740, 320, 890, 470, tag='〇×')
    
def draw23(event):
    canvas.create_oval(970, 320, 1120, 470, tag='〇×')

#３行目
def draw31(event):
    canvas.create_oval(500, 550, 650, 700, tag='〇×')
    
def draw32(event):
    canvas.create_oval(740, 550, 890, 700, tag='〇×')
    
def draw33(event):
    canvas.create_oval(970, 550, 1120, 700, tag='〇×')

    
#「消す」ボタンが押されたら
def reset(event):
    canvas.delete('〇×')

def func():
    print('Hello World')

#キャンバスエリア
canvas = tkinter.Canvas(root, width = 1600, height = 1200)

#縦線
canvas.create_line(925, 80, 925, 720)
canvas.create_line(700, 80, 700, 720)

#横線
canvas.create_line(450, 277, 1150, 277)
canvas.create_line(450, 514, 1150, 514)


#キャンバスバインド
canvas.place(x=0, y=0)


def start(event):
    #
    # 〇ボタン
    #
    #１行目
    button_draw11 = tkinter.Button(root, text='〇',width=3, command=func)
    button_draw11.bind('<Button>',draw11)
    button_draw11.place(x=560,y=160)

    button_draw12 = tkinter.Button(root, text='〇',width=3)
    button_draw12.bind('<Button>',draw12)
    button_draw12.place(x=800,y=160)

    button_draw13 = tkinter.Button(root, text='〇',width=3)
    button_draw13.bind('<Button>',draw13)
    button_draw13.place(x=1030,y=160)

    #2行目
    button_draw21 = tkinter.Button(root, text='〇',width=3)
    button_draw21.bind('<Button>',draw21)
    button_draw21.place(x=560,y=380)

    button_draw22 = tkinter.Button(root, text='〇',width=3)
    button_draw22.bind('<Button>',draw22)
    button_draw22.place(x=800,y=380)

    button_draw23 = tkinter.Button(root, text='〇',width=3)
    button_draw23.bind('<Button>',draw23)
    button_draw23.place(x=1030,y=380)

    #３行目
    button_draw31 = tkinter.Button(root, text='〇',width=3)
    button_draw31.bind('<Button>',draw31)
    button_draw31.place(x=560,y=610)

    button_draw32 = tkinter.Button(root, text='〇',width=3)
    button_draw32.bind('<Button>',draw32)
    button_draw32.place(x=800,y=610)

    button_draw33 = tkinter.Button(root, text='〇',width=3)
    button_draw33.bind('<Button>',draw33)
    button_draw33.place(x=1030,y=610)


#リセット
button_drawR = tkinter.Button(root, text='リセット',width=15)
button_drawR.bind('<Button-1>',reset)
button_drawR.place(x=350,y=350)


#スタート
button_drawS = tkinter.Button(root, text='スタート',width=15)
button_drawS.bind('<Button-1>',start)
button_drawS.place(x=150,y=350)


#
# GUIの末端
#
root.mainloop()

