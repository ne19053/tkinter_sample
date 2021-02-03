#-*- coding: utf-8 -*-
#tk25.pyw

import tkinter as tk
def get_text():
#"内容の取得（1行６文字から３行４文字まで"）
    print(tx.get('1.5','3.4'))

root = tk.Tk()
tx = tk.Text(width=30,height=5)
bt = tk.Button(text="1行６文字から３行４文字まで取得",command=get_text)
[widget.pack()for widget in(tx,bt)]
root.mainloop()
