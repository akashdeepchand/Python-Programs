from tkinter import *

box = Tk()


mb = Menu(box)
box.config(menu=mb)
########################################

fm = Menu(mb)
mb.add_cascade(label='File',menu=fm)

def nm_fun():
    print('This is a New Menu FUnction.')

nm = Menu(fm)
fm.add_command(label = 'New',command=nm_fun)

fm.add_separator()

om = Menu(fm)
fm.add_cascade(label='Open',menu=om)



def f_and_d(x):
    print(f"This is {x}")

ofm = Menu(om)
om.add_command(label='Open_FILE',command=lambda : f_and_d('file'))

odm = Menu(om)
om.add_command(label='Open_DIR',command=lambda : f_and_d('directory'))


#########################################

vm = Menu(mb)
mb.add_cascade(label='View',menu=vm)

tm = Menu(vm)
vm.add_cascade(label='tools',menu=tm)

def abc():
    print("This is a ScrewDriver")

screw = Menu(tm)
tm.add_command(label="Screwdriver",command=abc)


cm = Menu(vm)

i = StringVar()
vm.add_checkbutton(label='Context',variable=i,onvalue='On',offvalue='Off')

#######################################

em = Menu(mb)
mb.add_cascade(label='Edit',menu=em)

########################################

def action():
    print(f'Spinbox : {sb.get()}'
          f'\nMenu Check Button: {i.get()}')
    can.delete('all')

sb = Spinbox(box, from_= 0, to_=100)
sb.pack()



def new_fun(e):
    x1 , y1 = (e.x - 1) , (e.y - 1)
    x2 , y2 = (e.x + 1) , (e.y + 1)
    can.create_line(x1,y1,x2,y2,fill='blue',width=5)


can = Canvas(box, height=500,width=500,bg='yellow')
can.pack()
can.bind("<B1-Motion>",new_fun)


# can.create_line(10,50,110,150,fill='blue',width=5)
# can.create_rectangle(50,50,150,100,fill='blue',width=5,outline='white')
# # can.create_oval(200,200,400,450)
# can.create_polygon(250,20,200,100,100,130,200
#                    ,200,150,250,250,200,300,250
#                    ,270,200,300,130,270,100)



b1 = Button(box,text='Click ME.!!',bg='yellow',fg='blue',command=action)
b1.pack()

box.mainloop()
