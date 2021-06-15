from tkinter import *
from tkinter import messagebox


val = ""
A = 0
operator = ""


def button_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def button_2_isclicked():
    global val
    val = val +"2"
    data.set(val)

def button_3_isclicked():
    global val
    val = val +"3"
    data.set(val)

def button_4_isclicked():
    global val
    val = val +"4"
    data.set(val)

def button_5_isclicked():
    global val
    val = val +"5"
    data.set(val)

def button_6_isclicked():
    global val
    val = val +"6"
    data.set(val)

def button_7_isclicked():
    global val
    val = val +"7"
    data.set(val)

def button_8_isclicked():
    global val
    val = val +"8"
    data.set(val)

def button_9_isclicked():
    global val
    val = val +"9"
    data.set(val)

def button_0_isclicked():
    global val
    val = val +"0"
    data.set(val)


def button_plus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def button_minus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def button_mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def button_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

    
def c_pressed():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)



def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val = str(c)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val = str(c)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val = str(c)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error","Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            c = int(A / x)
            data.set(c)
            val = str(c)



calc =Tk()
calc.geometry("200x300")
calc.resizable(0,0)
calc.title("Calculator")


data = StringVar()
lb1 = Label(
    calc,
    text = "Label",
    anchor = SE,
    font = ("verdana",20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lb1.pack(expand=True, fill="both")

b1 = Frame(calc,bg="#000000")
b1.pack(expand = True, fill= "both")

b2 = Frame(calc)
b2.pack(expand = True, fill= "both")

b3 = Frame(calc)
b3.pack(expand = True, fill= "both")

b4 = Frame(calc)
b4.pack(expand = True, fill= "both")



button1 = Button(
    b1,
    text="1",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = button_1_isclicked,
)
button1.pack(side = LEFT, expand= True, fill="both")

button2 = Button(
    b1,
    text="2",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = button_2_isclicked,
)
button2.pack(side = LEFT, expand= True, fill="both")

button3 = Button(
    b1,
    text="3",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = button_3_isclicked,
)
button3.pack(side = LEFT, expand= True, fill="both")

buttonplus = Button(
    b1,
    text="+",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command=button_plus_clicked,
)
buttonplus.pack(side = LEFT, expand= True, fill="both")


button4 = Button(
    b2,
    text="4",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = button_4_isclicked,
)
button4.pack(side = LEFT, expand= True, fill="both")

button5 = Button(
    b2,
    text="5",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = button_5_isclicked,
)
button5.pack(side = LEFT, expand= True, fill="both")

button6 = Button(
    b2,
    text="6",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = button_6_isclicked,
)
button6.pack(side = LEFT, expand= True, fill="both")

buttonminus = Button(
    b2,
    text="-",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command=button_minus_clicked,
)
buttonminus.pack(side = LEFT, expand= True, fill="both")



button7 = Button(
    b3,
    text="7",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = button_7_isclicked,
)
button7.pack(side = LEFT, expand= True, fill="both")

button8 = Button(
    b3,
    text="8",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = button_8_isclicked,
)
button8.pack(side = LEFT, expand= True, fill="both")

button9 = Button(
    b3,
    text="9",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = button_9_isclicked,
)
button9.pack(side = LEFT, expand= True, fill="both")

buttonmul = Button(
    b3,
    text="*",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command=button_mul_clicked,
)
buttonmul.pack(side = LEFT, expand= True, fill="both")



buttonc = Button(
    b4,
    text="c",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = c_pressed,
)
buttonc.pack(side = LEFT, expand= True, fill="both")


button0 = Button(
    b4,
    text="0",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = button_0_isclicked,
)
button0.pack(side = LEFT, expand= True, fill="both")

buttonequal = Button(
    b4,
    text="=",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command = result,
)
buttonequal.pack(side = LEFT, expand= True, fill="both")

buttondiv = Button(
    b4,
    text="/",
    font = ("verdana",22),
    relief=GROOVE,
    border=0,
    command=button_div_clicked,
)
buttondiv.pack(side = LEFT, expand= True, fill="both")


calc.mainloop()
