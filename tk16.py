#-*- coding: utf-8 -*-
#tk16.pyw

import tkinter as tk
def btn_press():
    print("ボタンがおされました")
root = tk.Tk()
root.geometry("150x80")
#ボタンの作成、commandオプションで押し下げたときに呼び出す関数を指定できる。
bt = tk.Button(text="ボタン", command=btn_press)
bt.pack()
root.mainloop()