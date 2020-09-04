from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('100x100+500+200')
l2 = []  # occupied room
l1 = ['two-seater', 'three-seater', 'four-seater']  # total room
def f1():
    for i in range(len(l2)):
        if l2[i] in l1:
            print('yes-1')
            l1.remove(l2[i])
            print(l1)
            c['value'] = l1
        break
    if not l2:
        print('yes-2')
        c['value']=l1
c = ttk.Combobox(root, postcommand=f1)
c.pack()

mainloop()
