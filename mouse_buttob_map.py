from tkinter import *
box = Tk()

def lc(a):
    print(f'Left Click')

def rc(a):
    print("Right Click")

def mc(a):
    print('Middle CLick.')


bu = Button(box,text='Click')
bu.pack()
bu.bind("<Button-1>",lc)
bu.bind("<Button-2>",mc)
bu.bind("<Button-3>",rc)

box.mainloop()
