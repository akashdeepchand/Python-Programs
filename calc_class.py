from tkinter import *

box = Tk()

def insert_num(x):
    en.insert(END,x)

box.title('Calculator')

en = Entry(box,width=30,fg='blue')
en.pack(fill=X,expand=True)

f1 = Frame(box)
f1.pack(expand=True,fill=X)

b9 =Button(f1,text='9',command=lambda:insert_num(9))
b9.pack(side='left',expand=True,fill=X)

b8 =Button(f1,text='8',command=lambda:insert_num(8))
b8.pack(side='left',expand=True,fill=X)

b7 =Button(f1,text='7',command=lambda:insert_num(7))
b7.pack(side='left',expand=True,fill=X)

b_add =Button(f1,text='+',command=lambda:insert_num('+'))
b_add.pack(side='left',expand=True,fill=X)

f2 = Frame(box)
f2.pack(expand=True,fill=X)

b6 =Button(f2,text='6',command=lambda:insert_num(6))
b6.pack(side='left',expand=True,fill=X)

b5 =Button(f2,text='5',command=lambda:insert_num(5))
b5.pack(side='left',expand=True,fill=X)

b4 =Button(f2,text='4',command=lambda:insert_num(4))
b4.pack(side='left',expand=True,fill=X)

b_sub =Button(f2,text='-',command=lambda:insert_num("-"))
b_sub.pack(side='left',expand=True,fill=X)

f3 = Frame(box)
f3.pack(expand=True,fill=X)

b3 =Button(f3,text='3',command=lambda:insert_num(3))
b3.pack(side='left',expand=True,fill=X)

b2 =Button(f3,text='2',command=lambda:insert_num(2))
b2.pack(side='left',expand=True,fill=X)

b1 =Button(f3,text='1',command=lambda:insert_num(1))
b1.pack(side='left',expand=True,fill=X)

b_mul =Button(f3,text='',command=lambda:insert_num(''))
b_mul.pack(side='left',expand=True,fill=X)

f4 = Frame(box)
f4.pack(expand=True,fill=X)

b0 =Button(f4,text='0',command=lambda:insert_num(0))
b0.pack(side='left',expand=True,fill=X)

b_dot =Button(f4,text='.',command=lambda:insert_num("."))
b_dot.pack(side='left',expand=True,fill=X)



can =Button(f4,text='<')
can.pack(side='left',expand=True,fill=X)

b_div =Button(f4,text='/',command=lambda:insert_num('/'))
b_div.pack(side='left',expand=True,fill=X)

f5 = Frame(box)
f5.pack(expand=True,fill=X)

def clear():
    en.delete(0,END)
    en.insert(0,0)

clr = Button(f5,text='Clear ALL',command=clear)
clr.pack(side='left',expand=True,fill=X)

def total():
    ans = en.get()
    clear()
    en.insert(0, eval(ans))

b_eq =  Button(f5,text='Total',command=total)
b_eq.pack(side='left',expand=True,fill=X)

box.mainloop()
