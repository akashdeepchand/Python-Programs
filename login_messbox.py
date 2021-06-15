from tkinter import *
from tkinter import messagebox

box = Tk()
box.title('Login Page!')

f1 = Frame(box)
f2 = Frame(box)
f1.pack()
f2.pack()

l1 = Label(f1,text='Username :')
l1.pack(side='left')

l2 = Label(f2,text='Password :')
l2.pack(side='left')

e1 = Entry(f1,width=30,bg='red',fg='white')
e1.pack()

e2 = Entry(f2,width=30)
e2.pack()
e2.config(show='#')

def action():
    messagebox.askquestion(title='Bye',message='Ru sure?')
    # un =
    # pwd =
    print(f'{e1.get()} is {type(e1.get())}')
    e1.delete(0,END)
    e2.delete(0, END)


b = Button(box,text="Login Now!!!",bg='red',command=action)
b.pack()


box.mainloop()
