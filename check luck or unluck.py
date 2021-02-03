import tkinter as tk
import random

fortunes = ['大吉','吉','中吉','小吉','悩']
additional_msg = ['持ち人来たらず','商']

def predict():
    ms['text'] = random.choice(fortunes)
    ms['text'] = random.choice(additonal_msg)

root = tk.Tk()
root.geometry('300x200+400+200')
root.title('Fortune Cookie')
btl = tk.Button(text = 'Tell Fortune', command=predict)
ms = tk.Message(width=100,fg='blue',font='HG行書体')
btl.pack()
ms.pack(pady=50)
ms2.pack(pady=100)

root.mainloop()