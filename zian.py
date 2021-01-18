
from pynput.keyboard import Key, Controller
from pynput.mouse import Buttonnn, mouseController
import time
import os
import random
import 祖安语录

from tkinter import *
i = 0
now = False
mouse = mouseController()
keyboard = Controller()

window = Tk()

def intowechat():



    cli=os.popen("C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
    cli.close()
    mouse.position = (400, 150)
    mouse.click(Buttonnn.left, 2)
    mouse.move(260, -10)
    mouse.click(Buttonnn.left, 1)


def swkgoodnight():
    mouse.position = (400, 90)
    print(format(mouse.position))
    mouse.press(Buttonnn.left)
    mouse.release(Buttonnn.left)
    mouse.click(Buttonnn.left, 1)
    keyboard.type((renmin.get()))
    mouse.move(-30, 65)
    time.sleep(2)
    print(format(mouse.position))
    mouse.press(Buttonnn.left)
    mouse.release(Buttonnn.left)
    #
    time.sleep(1)

    keyboard.type((neir.get()))

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def 清理():
    mouse.position = (400, 150)
    mouse.click(Buttonnn.left, 2)
    mouse.move(260, -10)
    mouse.click(Buttonnn.left, 1)


def 祖安模式():
    mouse.position = (400, 90)
    print(format(mouse.position))
    mouse.press(Buttonnn.left)
    mouse.release(Buttonnn.left)
    mouse.click(Buttonnn.left, 1)
    keyboard.type((zumin.get()))
    mouse.move(-30, 70)
    time.sleep(2)
    print(format(mouse.position))
    mouse.press(Buttonnn.left)
    mouse.release(Buttonnn.left)
    time.sleep(1)
    for inn in range(0, int(zanumber.get())):
        keyboard.type(祖安语录.arr[random.randint(0, 40)])
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


# while True:
# clock=datetime.now()

# if clock.hour==17 and clock.minute==39 and clock.second==40:
# intowechat()
# 祖安模式()
# swkgoodnight()
# 清理()

def Buttonn():
    global i
    label.config(text="语言模式")
    i = 1


def 现在发():
    global now
    if now==False:
        now = True
        xianzai.config(text="现在发模式")

    elif now==True:
        now=False
        xianzai.config(text="定时发模式")



def gogogo():

    if i == 1:
        if now == True:
            intowechat()
            swkgoodnight()
            清理()
        else:
            run=True
            while run:
                if time.strftime("%H") == (shi.get()) and time.strftime("%M") == (fen.get()) and time.strftime("%S") == (miao.get()):
                    run=False
                    intowechat()
                    swkgoodnight()
                    清理()

    if i == 2:
        if now == True:
            intowechat()
            祖安模式()
            清理()
        else:

            run = True
            while run:
                if time.strftime("%H") == (shi.get()) and time.strftime("%M") == (fen.get()) and time.strftime(
                        "%S") == (miao.get()):
                    run = False
                    intowechat()
                    祖安模式()
                    清理()


def ButtonClick():
    global i
    # (textBox.get())
    label.config(text="祖安模式")
    i = 2
def get():

    timeclock2=time.strftime("%H:%M:%S")

    clock=Label(window,text=timeclock2,font=28)
    clock.configure(text=timeclock2)
    clock.grid(row=100,column=100)
    clock.after(200,get)

get()
window.title("自动发话")
window.geometry("600x300+200+250")

label = Label(window, width=0, height=0, text="请选择类型")
label.grid(row=0, column=2)

l = Label(window, width=0, height=0, text="请选择名字")
l.grid(row=2, column=0)
zunumber = Label(window, width=0, height=0, text="发送个数")
zunumber.grid(row=9, column=10)
zi = Label(window, width=0, height=0, text="请写内容")
zi.grid(row=9, column=0)
zanumber = Entry(window, width=10)
zanumber.grid(row=9, column=3)
button = Button(window, text="祖安模式", width=10, command=ButtonClick)
button.grid(row=1, column=3)
button = Button(window, text="语言模式", width=10, command=Buttonn)
button.grid(row=1, column=1)

renmin = Entry(window, width=10)
renmin.grid(row=2, column=1)
neir = Entry(window, width=10)
neir.grid(row=9, column=1)
button = Button(window, text="开始", width=10, command=gogogo)
button.grid(row=100, column=2)
xianzai = Button(window, text="定时发模式", width=10, command=现在发)
xianzai.grid(row=10, column=2)
zumin = Entry(window, width=10)
zumin.grid(row=2, column=3)

shi = Entry(window, width=10)
shi.grid(row=3, column=2)

fen = Entry(window, width=10)
fen.grid(row=4, column=2)
miao = Entry(window, width=10)
miao.grid(row=5, column=2)
la = Label(window, width=0, height=0, text="请选择小时")
la.grid(row=3, column=0)
lab = Label(window, width=0, height=0, text="请选择分钟")
lab.grid(row=4, column=0)
labe = Label(window, width=0, height=0, text="请选择秒")
labe.grid(row=5, column=0)
mainloop()
