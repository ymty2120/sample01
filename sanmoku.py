#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter
import random


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
rN = 0 #乱数用
ForS = 0 #スタートボタン回数制限用
win = 0 #合計勝利数計算用
lose = 0 #合計敗北数計算用
draw = 0 #合計引き分け数計算用
#######################################################

#勝敗判定変数とキャンバスの初期化
#######################################################
def canvasReset():
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
    firstOrSecond()
#######################################################


#先行後攻決定
#######################################################
def firstOrSecond():
    rN = random.randint(1, 10) #先行後攻決定乱数
    if rN >= 6:
        rN = random.randint(1, 10)
        if rN >= 2:
            firstAction()
        else:
            randomAction()
#######################################################


#先行行動
#######################################################
def firstAction():
    global a, c, g, i
    rN = random.randint(1, 4)
    if rN == 1:
        canvas.create_line(500, 250, 650, 100, fill='red', tag='〇×')
        canvas.create_line(650, 250, 500, 100, fill='red', tag='〇×')
        a = 2
    elif rN == 2:
        canvas.create_line(970, 250, 1120, 100, fill='red', tag='〇×')
        canvas.create_line(1120, 250, 970, 100, fill='red', tag='〇×')
        c = 2
    elif rN == 3:
        canvas.create_line(500, 550, 650, 700, fill='red', tag='〇×')
        canvas.create_line(650, 550, 500, 700, fill='red', tag='〇×')
        g = 2
    else:
        canvas.create_line(970, 550, 1120, 700, fill='red', tag='〇×')
        canvas.create_line(1120, 550, 970, 700, fill='red', tag='〇×')
        i = 2
#######################################################


#後攻行動
#######################################################
def secondAction():
    global e
    rN = random.randint(1, 10)
    if rN >= 2:
        canvas.create_line(740, 320, 890, 470, fill='red', tag='〇×')
        canvas.create_line(890, 320, 740, 470, fill='red', tag='〇×')
        e = 2
    else:
        randomAction()
#######################################################


#行動パターン
#######################################################
def actionPattern():
#パターンa
    global a, b, c, d, e, f, g, h, i
    if a >= 1 and c >= 1 and b == 0:
        canvas.create_line(740, 250, 890, 100, fill='red', tag='〇×')
        canvas.create_line(890, 250, 740, 100, fill='red', tag='〇×')
        b = 2
    elif a >= 1 and b >= 1 and c ==0:
        canvas.create_line(970, 250, 1120, 100, fill='red', tag='〇×')
        canvas.create_line(1120, 250, 970, 100, fill='red', tag='〇×')
        c = 2
    elif a >= 1 and e >= 1 and i == 0:
        canvas.create_line(970, 550, 1120, 700, fill='red', tag='〇×')
        canvas.create_line(1120, 550, 970, 700, fill='red', tag='〇×')
        i = 2
    elif a >= 1 and d >= 1 and g == 0:
        canvas.create_line(500, 550, 650, 700, fill='red', tag='〇×')
        canvas.create_line(650, 550, 500, 700, fill='red', tag='〇×')
        g = 2
    elif a >= 1 and i >= 1 and e == 0:
        canvas.create_line(740, 320, 890, 470, fill='red', tag='〇×')
        canvas.create_line(890, 320, 740, 470, fill='red', tag='〇×')
        e = 2
    elif a >= 1 and g >= 1 and d == 0:
        canvas.create_line(500, 320, 650, 470, fill='red', tag='〇×')
        canvas.create_line(650, 320, 500, 470, fill='red', tag='〇×')
        d = 2
#パターンb
    elif b >= 1 and c >= 1 and a == 0:
        canvas.create_line(500, 250, 650, 100, fill='red', tag='〇×')
        canvas.create_line(650, 250, 500, 100, fill='red', tag='〇×')
        a = 2
    elif b >= 1 and e >= 1 and h == 0:
        canvas.create_line(740, 550, 890, 700, fill='red', tag='〇×')
        canvas.create_line(890, 550, 740, 700, fill='red', tag='〇×')
        h = 2
    elif b >= 1 and h >= 1 and e == 0:
        canvas.create_line(740, 320, 890, 470, fill='red', tag='〇×')
        canvas.create_line(890, 320, 740, 470, fill='red', tag='〇×')
        e = 2
#パターンc
    elif c >= 1 and f >= 1 and i == 0:
        canvas.create_line(970, 550, 1120, 700, fill='red', tag='〇×')
        canvas.create_line(1120, 550, 970, 700, fill='red', tag='〇×')
        i = 2
    elif c >= 1 and i >= 1 and f == 0:
        canvas.create_line(970, 320, 1120, 470, fill='red', tag='〇×')
        canvas.create_line(1120, 320, 970, 470, fill='red', tag='〇×')
        f = 2
    elif c >= 1 and e >= 1 and g == 0:
        canvas.create_line(500, 550, 650, 700, fill='red', tag='〇×')
        canvas.create_line(650, 550, 500, 700, fill='red', tag='〇×')
        g = 2
    elif c >= 1 and g >= 1 and e == 0:
        canvas.create_line(740, 320, 890, 470, fill='red', tag='〇×')
        canvas.create_line(890, 320, 740, 470, fill='red', tag='〇×')
        e = 2
#パターンd
    elif d >= 1 and g >= 1 and a == 0:
        canvas.create_line(500, 250, 650, 100, fill='red', tag='〇×')
        canvas.create_line(650, 250, 500, 100, fill='red', tag='〇×')
        a = 2
    elif d >= 1 and  e >= 1 and f == 0:
        canvas.create_line(970, 320, 1120, 470, fill='red', tag='〇×')
        canvas.create_line(1120, 320, 970, 470, fill='red', tag='〇×')
        f = 2
    elif d >= 1 and f >= 1 and e == 0:
        canvas.create_line(740, 320, 890, 470, fill='red', tag='〇×')
        canvas.create_line(890, 320, 740, 470, fill='red', tag='〇×')
        e = 2
#パターンe
    elif e >= 1 and h >= 1 and b == 0:
        canvas.create_line(740, 250, 890, 100, fill='red', tag='〇×')
        canvas.create_line(890, 250, 740, 100, fill='red', tag='〇×')
        b = 2
    elif e >= 1 and f >= 1 and d == 0:
        canvas.create_line(500, 320, 650, 470, fill='red', tag='〇×')
        canvas.create_line(650, 320, 500, 470, fill='red', tag='〇×')
        d = 2
    elif e >= 1 and i >= 1 and a == 0:
        canvas.create_line(500, 250, 650, 100, fill='red', tag='〇×')
        canvas.create_line(650, 250, 500, 100, fill='red', tag='〇×')
        a = 2
    elif e >= 1 and g >= 1 and c == 0:
        canvas.create_line(970, 250, 1120, 100, fill='red', tag='〇×')
        canvas.create_line(1120, 250, 970, 100, fill='red', tag='〇×')
        c = 2
#パターンf
    elif f >= 1 and i >= 1 and c == 0:
        canvas.create_line(970, 250, 1120, 100, fill='red', tag='〇×')
        canvas.create_line(1120, 250, 970, 100, fill='red', tag='〇×')
        c = 2
#パターンg
    elif g >= 1 and h >= 1 and i == 0:
        canvas.create_line(970, 550, 1120, 700, fill='red', tag='〇×')
        canvas.create_line(1120, 550, 970, 700, fill='red', tag='〇×')
        i = 2
    elif g >= 1 and i >= 1 and h == 0:
        canvas.create_line(740, 550, 890, 700, fill='red', tag='〇×')
        canvas.create_line(890, 550, 740, 700, fill='red', tag='〇×')
        h = 2
#パターンh
    elif h >= 1 and i >= 1 and g == 0:
        canvas.create_line(500, 550, 650, 700, fill='red', tag='〇×')
        canvas.create_line(650, 550, 500, 700, fill='red', tag='〇×')
        g = 2
    else:
        randomAction()
#######################################################


#ランダム行動
#######################################################
def randomAction():
    global a, b, c, d, e, f, g, h, i
    rN = random.randint(1, 9)
    if rN == 1 and a == 0:
        canvas.create_line(500, 250, 650, 100, fill='red', tag='〇×')
        canvas.create_line(650, 250, 500, 100, fill='red', tag='〇×')
        a = 2
    elif rN == 2 and b == 0:
        canvas.create_line(740, 250, 890, 100, fill='red', tag='〇×')
        canvas.create_line(890, 250, 740, 100, fill='red', tag='〇×')
        b = 2
    elif rN == 3 and c == 0:
        canvas.create_line(970, 250, 1120, 100, fill='red', tag='〇×')
        canvas.create_line(1120, 250, 970, 100, fill='red', tag='〇×')
        c = 2
    elif rN == 4 and d == 0:
        canvas.create_line(500, 320, 650, 470, fill='red', tag='〇×')
        canvas.create_line(650, 320, 500, 470, fill='red', tag='〇×')
        d = 2
    elif rN == 5 and e == 0:
        canvas.create_line(740, 320, 890, 470, fill='red', tag='〇×')
        canvas.create_line(890, 320, 740, 470, fill='red', tag='〇×')
        e = 2
    elif rN == 6 and f == 0:
        canvas.create_line(970, 320, 1120, 470, fill='red', tag='〇×')
        canvas.create_line(1120, 320, 970, 470, fill='red', tag='〇×')
        f = 2
    elif rN == 7 and g == 0:
        canvas.create_line(500, 550, 650, 700, fill='red', tag='〇×')
        canvas.create_line(650, 550, 500, 700, fill='red', tag='〇×')
        g = 2
    elif rN == 8 and h == 0:
        canvas.create_line(740, 550, 890, 700, fill='red', tag='〇×')
        canvas.create_line(890, 550, 740, 700, fill='red', tag='〇×')
        h = 2
    elif rN ==9 and i == 0:
        canvas.create_line(970, 550, 1120, 700, fill='red', tag='〇×')
        canvas.create_line(1120, 550, 970, 700, fill='red', tag='〇×')
        i = 2
    elif a >=1 and b >= 1 and c >= 1 and d >=1 and e >= 1 and f >= 1 and g >=1 and h >= 1 and i >= 1:
        pass
    else:
        randomAction()
#######################################################


#〇×描画
#######################################################
#１行目
def draw11(event):
    global a, b, c, d, e, f, g, h, i
    if a == 0:
        canvas.create_oval(500, 250, 650, 100, tag='〇×')
        a = 1
        if a <= 1 and b <= 1 and c <= 1 and d <= 1 and e <= 1 and f <= 1 and g <= 1 and h <= 1 and i <= 1:
            secondAction()
        else:
            rN = random.randint(1, 10)
            if rN >= 2:
                actionPattern()
            else:
                randomAction()

def draw12(event):
    global a, b, c, d, e, f, g, h, i
    if b == 0:
        canvas.create_oval(740, 250, 890, 100, tag='〇×')
        b = 1
        if a <= 1 and b <= 1 and c <= 1 and d <= 1 and e <= 1 and f <= 1 and g <= 1 and h <= 1 and i <= 1:
            secondAction()
        else:
            rN = random.randint(1, 10)
            if rN >= 2:
                actionPattern()
            else:
                randomAction()

def draw13(event):
    global a, b, c, d, e, f, g, h, i
    if c == 0:
        canvas.create_oval(970, 250, 1120, 100, tag='〇×')
        c = 1
        if a <= 1 and b <= 1 and c <= 1 and d <= 1 and e <= 1 and f <= 1 and g <= 1 and h <= 1 and i <= 1:
            secondAction()
        else:
            rN = random.randint(1, 10)
            if rN >= 2:
                actionPattern()
            else:
                randomAction()

#２行目
def draw21(event):
    global a, b, c, d, e, f, g, h, i
    if d == 0:
        canvas.create_oval(500, 320, 650, 470, tag='〇×')
        d = 1
        if a <= 1 and b <= 1 and c <= 1 and d <= 1 and e <= 1 and f <= 1 and g <= 1 and h <= 1 and i <= 1:
            secondAction()
        else:
            rN = random.randint(1, 10)
            if rN >= 2:
                actionPattern()
            else:
                randomAction()
    
def draw22(event):
    global a, b, c, d, e, f, g, h, i
    if e == 0:
        canvas.create_oval(740, 320, 890, 470, tag='〇×')
        e = 1
        if a <= 1 and b <= 1 and c <= 1 and d <= 1 and e <= 1 and f <= 1 and g <= 1 and h <= 1 and i <= 1:
            secondAction()
        else:
            rN = random.randint(1, 10)
            if rN >= 2:
                actionPattern()
            else:
                randomAction()
    
def draw23(event):
    global a, b, c, d, e, f, g, h, i
    if f == 0:
        canvas.create_oval(970, 320, 1120, 470, tag='〇×')
        f = 1
        if a <= 1 and b <= 1 and c <= 1 and d <= 1 and e <= 1 and f <= 1 and g <= 1 and h <= 1 and i <= 1:
            secondAction()
        else:
            rN = random.randint(1, 10)
            if rN >= 2:
                actionPattern()
            else:
                randomAction()

#３行目
def draw31(event):
    global a, b, c, d, e, f, g, h, i
    if g == 0:
        canvas.create_oval(500, 550, 650, 700, tag='〇×')
        g = 1
        if a <= 1 and b <= 1 and c <= 1 and d <= 1 and e <= 1 and f <= 1 and g <= 1 and h <= 1 and i <= 1:
            secondAction()
        else:
            rN = random.randint(1, 10)
            if rN >= 2:
                actionPattern()
            else:
                randomAction()
    
def draw32(event):
    global a, b, c, d, e, f, g, h, i
    if h == 0:
        canvas.create_oval(740, 550, 890, 700, tag='〇×')
        h = 1
        if a <= 1 and b <= 1 and c <= 1 and d <= 1 and e <= 1 and f <= 1 and g <= 1 and h <= 1 and i <= 1:
            secondAction()
        else:
            rN = random.randint(1, 10)
            if rN >= 2:
                actionPattern()
            else:
                randomAction()
    
def draw33(event):
    global a, b, c, d, e, f, g, h, i
    if i == 0:
        canvas.create_oval(970, 550, 1120, 700, tag='〇×')
        i = 1
        if a <= 1 and b <= 1 and c <= 1 and d <= 1 and e <= 1 and f <= 1 and g <= 1 and h <= 1 and i <= 1:
            secondAction()
        else:
            rN = random.randint(1, 10)
            if rN >= 2:
                actionPattern()
            else:
                randomAction()
#######################################################


#リセット
#######################################################
def reset(event):
    if ForS == 1:
        canvasReset()
#######################################################


#勝敗判定
#######################################################
def funcWL():
    global win, lose, draw
#勝利
    if a == 1 and b == 1 and c == 1 or a == 1 and d == 1 and g == 1 or a == 1 and e == 1 and i == 1 or b == 1 and e == 1 and h == 1 or c == 1 and f == 1 and i == 1 or c == 1 and e == 1 and g == 1 or d == 1 and e == 1 and f == 1 or g == 1 and h == 1 and i == 1:
        print('WIN')
        win += 1
        canvasReset()
#敗北
    elif a == 2 and b == 2 and c == 2 or a == 2 and d == 2 and g == 2 or a == 2 and e == 2 and i == 2 or b == 2 and e == 2 and h == 2 or c == 2 and f == 2 and i == 2 or c == 2 and e == 2 and g == 2 or d == 2 and e == 2 and f == 2 or g == 2 and h == 2 and i == 2:
        print('LOSE')
        lose += 1
        canvasReset()
#引き分け
    elif a >= 1 and b >= 1 and c >= 1 and d >= 1 and e >= 1 and f >= 1 and g >= 1 and h >= 1 and i >= 1:
        print('DRAW')
        draw += 1
        canvasReset()
#######################################################


#戦績
#######################################################
def countWL(event):
    print(f'WIN:{win}  LOSE:{lose}  DRAW:{draw}')
#######################################################


#戦績リセット
#######################################################
def countReset(event):
    global win, lose, draw
    win = 0
    lose = 0
    draw = 0
    print(f'戦績がリセットされました')
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


#スタート処理
#######################################################
def start(event):
    global ForS
    if ForS == 0:
        ForS = 1
        firstOrSecond()
#〇ボタン
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


#戦績ボタン
#######################################################
button_countWL = tkinter.Button(root, text='戦績',width=15)
button_countWL.bind('<Button-1>',countWL)
button_countWL.place(x=50,y=500)
#######################################################


#戦績リセットボタン
#######################################################
button_countWL = tkinter.Button(root, text='戦績リセット',width=15)
button_countWL.bind('<Button-1>',countReset)
button_countWL.place(x=250,y=500)
#######################################################


#リセットボタン
#######################################################
button_drawR = tkinter.Button(root, text='リセット',width=15)
button_drawR.bind('<Button-1>',reset)
button_drawR.place(x=250,y=300)
#######################################################


#スタートボタン
#######################################################
button_drawS = tkinter.Button(root, text='スタート',width=15)
button_drawS.bind('<Button-1>',start)
button_drawS.place(x=50,y=300)
#######################################################


#説明
#######################################################
print('最初の１回目はスタートボタンを押してください')
print('先行後攻はランダムに決まります')
#######################################################


#ループ
#######################################################
root.mainloop()
#######################################################

