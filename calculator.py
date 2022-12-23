from tkinter import *
from turtle import color
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=35)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def buttonClear():
    e.delete(0, END)

def buttonAdd():
    firstNumber = e.get()
    global fNum 
    fNum = int(firstNumber)
    e.delete(0, END)

def buttonEqualTo():
    secondNumber = e.get()
    e.delete(0, END)
    e.insert(0, fNum + int(secondNumber))

#define buttons
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))
buttonAddition = Button(root, text="+", padx=39, pady=20, command=buttonAdd)
buttonEqualTo = Button(root, text="=", padx=99, pady=20, command=buttonEqualTo)
buttonClear = Button(root, text="Clear", padx=90, pady=20, command=buttonClear)



#Put the buttons on the screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonAddition.grid(row=5, column=0)
buttonEqualTo.grid(row=5, column=1, columnspan=2) 


root.mainloop()