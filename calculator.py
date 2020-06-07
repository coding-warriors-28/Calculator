import tkinter as tk

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")


win = tk.Tk()
win.geometry("500x400")
win.title("Calculator")
win.configure(background = "black")

equation = tk.StringVar()

expression_field = tk.Entry(win,textvariable=equation,width=44,font=('Arial',16))
expression_field.place(x=0,y=30)
equation.set('enter your expression')

button1 = tk.Button(win, text=' 7 ', fg='black', bg='#fff645',command=lambda: press(7), height=2, width=15)
button1.place(x=10,y=80)

button2 = tk.Button(win, text=' 8 ', fg='black', bg='#fff645',command=lambda: press(8), height=2, width=15)
button2.place(x=130,y=80)

button3 = tk.Button(win, text=' 9 ', fg='black', bg='#fff645',command=lambda: press(9), height=2, width=15)
button3.place(x=250,y=80)

button4 = tk.Button(win, text=' 4 ', fg='black', bg='#fff645',command=lambda: press(4), height=2, width=15)
button4.place(x=10,y=140)

button5 = tk.Button(win, text=' 5 ', fg='black', bg='#fff645',command=lambda: press(5), height=2, width=15)
button5.place(x=130,y=140)

button6 = tk.Button(win, text=' 6 ', fg='black', bg='#fff645',command=lambda: press(6), height=2, width=15)
button6.place(x=250,y=140)

button7 = tk.Button(win, text=' 1 ', fg='black', bg='#fff645',command=lambda: press(1), height=2, width=15)
button7.place(x=10,y=200)

button8 = tk.Button(win, text=' 2 ', fg='black', bg='#fff645',command=lambda: press(2), height=2, width=15)
button8.place(x=130,y=200)

button9 = tk.Button(win, text=' 3 ', fg='black', bg='#fff645',command=lambda: press(3), height=2, width=15)
button9.place(x=250,y=200)

button0 = tk.Button(win, text=' 0 ', fg='black', bg='#fff645',command=lambda: press(0), height=2, width=15)
button0.place(x=130,y=260)

plus = tk.Button(win, text=' + ', fg='black', bg='#fff645',command=lambda: press("+"), height=2, width=15)
plus.place(x=370,y=80)

minus = tk.Button(win, text=' - ', fg='black', bg='#fff645',command=lambda: press("-"), height=2, width=15)
minus.place(x=370,y=140)


multiply = tk.Button(win, text=' * ', fg='black', bg='#fff645',command=lambda: press("*"), height=2, width=15)
multiply.place(x=370,y=200)

divide = tk.Button(win, text=' / ', fg='black', bg='#fff645',command=lambda: press("/"), height=2, width=15)
divide.place(x=370,y=260)

equal = tk.Button(win, text=' = ', fg='black', bg='#fff645',command=equalpress, height=2, width=15)
equal.place(x=250,y=260)

clear = tk.Button(win, text='Clear', fg='black', bg='#fff645',command=clear, height=2, width=15)
clear.place(x=175,y=320)

Decimal = tk.Button(win, text='.', fg='black', bg='#fff645',command=lambda: press('.'), height=2, width=15)
Decimal.place(x=10,y=260)

win.mainloop()
