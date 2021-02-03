#-*- coding: utf-8 -*-
#tk19.pyw

import tkinter as tk
#rootの定義をしないと .Stringvar()　使用時にエラーになる
root = tk.Tk()
strvar= tk.StringVar()
print(strvar)
print(type(strvar))