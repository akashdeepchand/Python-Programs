from tkinter import *
from tkinter.ttk import Combobox

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
    ans = lb.curselection()
    print(f'Username :{e1.get()} \nPassword: {e2.get()} \nCheckButton : {c.get()} '
          f'\nRadio Button : {r.get()}\n'
          f'Combobox : {cmb.get()}\n'
          f'List Box : { list(map(lb.get,ans))}\n'
          f'Slider: {sc.get()}')

    e1.delete(0,END)
    e2.delete(0, END)


c = StringVar()
cb = Checkbutton(box,text='I accept all terms & Conditions.',variable=c,onvalue='I Accept',offvalue='I Reject')
cb.pack()

r = StringVar()
rb1 = Radiobutton(box,text='male',value='Male',variable=r)
rb1.pack()

rb2 = Radiobutton(box,text='Female',value='FeMale',variable=r)
rb2.pack()

cmb_list = []
for i in range(1950,2022):
    cmb_list.append(i)

cmb = Combobox(box,values=cmb_list)
cmb.pack()

lb_list = ['Python','Java','C','C++','Ruby',"perl",'CSS',"HTML"]

lb = Listbox(box,selectmode=EXTENDED)
lb.insert(0,*lb_list)
lb.pack()

sc = Scale(box, from_=0,to_=500)
sc.pack()

b = Button(box,text="Login Now!!!",bg='red',command=action)
b.pack()

box.mainloop()
