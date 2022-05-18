#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter

#設定
#######################################################
root = tkinter.Tk()
root.title('三目並べ')
root.state('zoomed')
root.geometry('1600x1200')
#######################################################


#変数定義
#######################################################
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
win = 0
lose = 0
draw = 0
#######################################################


#〇描画
#######################################################
#１行目
def draw11(event):
    canvas.create_oval(500, 250, 650, 100, tag='〇×')
    global a
    a = 1

def draw12(event):
    canvas.create_oval(740, 250, 890, 100, tag='〇×')
    global b
    b = 1

def draw13(event):
    canvas.create_oval(970, 250, 1120, 100, tag='〇×')
    global c
    c = 1

#２行目
def draw21(event):
    canvas.create_oval(500, 320, 650, 470, tag='〇×')
    global d
    d = 1
    
def draw22(event):
    canvas.create_oval(740, 320, 890, 470, tag='〇×')
    global e
    e = 1
    
def draw23(event):
    canvas.create_oval(970, 320, 1120, 470, tag='〇×')
    global f
    f = 1

#３行目
def draw31(event):
    canvas.create_oval(500, 550, 650, 700, tag='〇×')
    global g
    g = 1
    
def draw32(event):
    canvas.create_oval(740, 550, 890, 700, tag='〇×')
    global h
    h = 1
    
def draw33(event):
    canvas.create_oval(970, 550, 1120, 700, tag='〇×')
    global i
    i = 1
#######################################################


#リセット
#######################################################
def reset(event):
    canvas.delete('〇×')
    global a, b, c, d, e, f, g, h, i
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
#######################################################

#勝敗判定
#######################################################
def funcWL():
    global a, b, c, d, e, f, g, h, i, win, lose, draw
#勝利
    if a == 1 and b == 1 and c == 1 or a == 1 and d == 1 and g == 1 or a == 1 and e == 1 and i == 1 or b == 1 and e == 1 and h == 1 or c == 1 and f == 1 and i == 1 or c == 1 and e == 1 and g == 1 or d == 1 and e == 1 and f == 1 or g == 1 and h == 1 and i == 1:
        print('WIN')
        win += 1
        canvas.delete('〇×')
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i = 0
#敗北
    elif a == 2 and b == 2 and c == 2 or a == 2 and d == 2 and g == 2 or a == 2 and e == 2 and i == 2 or b == 2 and e == 2 and h == 2 or c == 2 and f == 2 and i == 2 or c == 2 and e == 2 and g == 2 or d == 2 and e == 2 and f == 2 or g == 2 and h == 2 and i == 2:
        print('LOSE')
        lose += 1
        canvas.delete('〇×')
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i = 0
#引き分け

#######################################################

#戦績
#######################################################
def countWL(event):
    print(f'WIN:{win}  LOSE:{lose}  DRAW:{draw}')
#######################################################


#キャンバスエリア
#######################################################
canvas = tkinter.Canvas(root, width = 1600, height = 1200)
#######################################################


#縦線
#######################################################
canvas.create_line(925, 80, 925, 720)
canvas.create_line(700, 80, 700, 720)
#######################################################


#横線
#######################################################
canvas.create_line(450, 277, 1150, 277)
canvas.create_line(450, 514, 1150, 514)
#######################################################


#キャンバスバインド
#######################################################
canvas.place(x=0, y=0)
#######################################################


# 〇ボタン
#######################################################
#１行目
button_draw11 = tkinter.Button(root, text='〇',width=3, command=funcWL)
button_draw11.bind('<Button>',draw11)
button_draw11.place(x=560,y=160)

button_draw12 = tkinter.Button(root, text='〇',width=3, command=funcWL)
button_draw12.bind('<Button>',draw12)
button_draw12.place(x=800,y=160)

button_draw13 = tkinter.Button(root, text='〇',width=3, command=funcWL)
button_draw13.bind('<Button>',draw13)
button_draw13.place(x=1030,y=160)

#2行目
button_draw21 = tkinter.Button(root, text='〇',width=3, command=funcWL)
button_draw21.bind('<Button>',draw21)
button_draw21.place(x=560,y=380)

button_draw22 = tkinter.Button(root, text='〇',width=3, command=funcWL)
button_draw22.bind('<Button>',draw22)
button_draw22.place(x=800,y=380)

button_draw23 = tkinter.Button(root, text='〇',width=3, command=funcWL)
button_draw23.bind('<Button>',draw23)
button_draw23.place(x=1030,y=380)

#３行目
button_draw31 = tkinter.Button(root, text='〇',width=3, command=funcWL)
button_draw31.bind('<Button>',draw31)
button_draw31.place(x=560,y=610)

button_draw32 = tkinter.Button(root, text='〇',width=3, command=funcWL)
button_draw32.bind('<Button>',draw32)
button_draw32.place(x=800,y=610)

button_draw33 = tkinter.Button(root, text='〇',width=3, command=funcWL)
button_draw33.bind('<Button>',draw33)
button_draw33.place(x=1030,y=610)
#######################################################

#勝敗カウント
#######################################################
button_countWL = tkinter.Button(root, text='戦績',width=15)
button_countWL.bind('<Button-1>',countWL)
button_countWL.place(x=150,y=550)
#######################################################

#リセット
#######################################################
button_drawR = tkinter.Button(root, text='リセット',width=15)
button_drawR.bind('<Button-1>',reset)
button_drawR.place(x=350,y=350)
#######################################################


#スタート
#######################################################
#button_drawS = tkinter.Button(root, text='スタート',width=15)
#button_drawS.bind('<Button-1>',start)
#button_drawS.place(x=150,y=350)
#######################################################


#
# GUIの末端
#
root.mainloop()

