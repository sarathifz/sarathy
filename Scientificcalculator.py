from tkinter import *
import math as m

window= Tk()

window.minsize(520, 340)
window.maxsize(520, 340)

window.title("Scientific calutor")

window['bg'] = "#AFF7F2"

sc = StringVar()
sc = Entry(master=window, width=31, textvariable=sc, relief=SUNKEN, font="cosmicsansms 20",bg='#BEC5CE')
sc.grid(row=0, column=0, columnspan=10, padx=11, pady=12)



def sciCal(event):
    key = event.widget
    text = key['text']
    val = sc.get()
    sc.delete(0, END)
    if text == "sin":
        sc.insert(0, m.sin(float(val)))
    elif text == "cos":
        sc.insert(0, m.cos(float(val)))
    elif text == "tan":
        sc.insert(0, m.tan(float(val)))
    elif text == "log":
        if (float(val) <= 0.00):
            sc.insert(0, "Not Possible")
        else:
            sc.insert(0, m.log10(float(val)))
    elif text == "ln":
        if (float(val) <= 0.00):
            sc.insert(0, "Not Possible")
        else:
            sc.insert(0, m.log(float(val)))
    elif text == "√":
        sc.insert(0, m.sqrt(float(val)))
    elif text == "!":
        sc.insert(0, m.factorial(int(val)))
    elif text == "rad":
        sc.insert(0, m.radians(float(val)))
    elif text == "deg":
        sc.insert(0, m.degrees(float(val)))
    elif text == "1/x":
        if (val == "0"):
            sc.insert(0, "ꝏ")
        else:
            sc.insert(0, 1 / float(val))
    elif text == "π":
        if val == "":
            ans = str(m.pi)
            sc.insert(0, ans)
        else:
            ans = str(float(val) * (m.pi))
            sc.insert(0, ans)

    elif text == "e":
        if val == "":
            sc.insert(0, str(m.e))
        else:
            sc.insert(0, str(float(val) * (m.e)))


def click(event):
    key = event.widget
    text = key['text']
    oldValue = sc.get()
    sc.delete(0, END)
    newValue = oldValue + text
    sc.insert(0, newValue)


def clr(event):
    sc.delete(0, END)


def backspace(event):
    entered = sc.get()
    length = len(entered) - 1
    sc.delete(length, END)


def calculate(event):
    answer = sc.get()
    if "^" in answer:
        answer = answer.replace("^", "**")
    answer = eval(answer)
    sc.delete(0, END)
    sc.insert(0, answer)


class calutor:
    def __init__(self, txt, r, c, funcName, color="white"):
        self.var = Button(master=window, text=txt, padx=3, pady=5, fg="black", bg=color, width=10, font="cosmicsansms 12")
        self.var.bind("<Button-1>", funcName)
        self.var.grid(row=r, column=c)


btn0 = calutor("sin", 1, 0, sciCal)

btn1 = calutor("cos", 1, 1, sciCal)

btn2 = calutor("tan", 1, 2, sciCal)

btn3 = calutor("log", 1, 3, sciCal)

btn4 = calutor("ln", 1, 4, sciCal)

btn5 = calutor("(", 2, 0, click)

btn6 = calutor(")", 2, 1, click)

btn7 = calutor("^", 2, 2, click)

btn8 = calutor("√", 2, 3, sciCal)

btn9 = calutor("!", 2, 4, sciCal)

btn10 = calutor("π", 3, 0, sciCal)

btn11 = calutor("1/x", 3, 1, sciCal)

btn12 = calutor("deg", 3, 2, sciCal)

btn13 = calutor("rad", 3, 3, sciCal)

btn14 = calutor("e", 3, 4, sciCal)

btn15 = calutor("/", 4, 0, click)

btn16 = calutor("*", 4, 1, click)

btn17 = calutor("-", 4, 2, click)

btn18 = calutor("+", 4, 3, click)

btn19 = calutor("%", 4, 4, click)

btn20 = calutor("9", 5, 0, click)

btn21 = calutor("8", 5, 1, click)

btn22 = calutor("7", 5, 2, click)

btn23 = calutor("6", 5, 3, click)

btn24 = calutor("5", 5, 4, click)

btn25 = calutor("4", 6, 0, click)

btn26 = calutor("3", 6, 1, click)

btn27 = calutor("2", 6, 2, click)

btn28 = calutor("1", 6, 3, click)

btn29 = calutor("0", 6, 4, click)

btn30 = calutor("C", 7, 0, clr)

btn31 = calutor("⌦", 7, 1, backspace)

btn32 = calutor("00", 7, 2, click)

btn33 = calutor(".", 7, 3, click)

btn34 = calutor("=", 7, 4, calculate)

window.mainloop()