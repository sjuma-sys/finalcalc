from tkinter import *
import threading
#refrences https://www.youtube.com/watch?v=F5PfbC5ld-Q&t=484s, https://www.youtube.com/watch?v=XhCfsuMyhXo&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=6
window = Tk()
window.title("Calculator")

viewansr = Entry(window, width = 35, borderwidth=5)
viewansr.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def click(number): 
	value= viewansr.get()
	viewansr.delete(0, END)
	viewansr.insert(0,str(value) + str(number))
def clear():
	viewansr.delete(0, END)
def add():
	fistvalue = viewansr.get()
	global fistone
	fistone = int(fistvalue)
	viewansr.delete(0, END)
def equal():
	secone = viewansr.get()
	viewansr.delete(0, END)
	viewansr.insert(0, fistone + int(secone))

num1 = Button(window, text="1", padx=40, pady=20,command=lambda: click(1))
num2 = Button(window, text="2", padx=40, pady=20,command=lambda: click(2))
num3 = Button(window, text="3", padx=40, pady=20,command=lambda: click(3))
num4 = Button(window, text="4", padx=40, pady=20,command=lambda: click(4))
num5 = Button(window, text="5", padx=40, pady=20,command=lambda: click(5))
num6 = Button(window, text="6", padx=40, pady=20,command=lambda: click(6))
num7 = Button(window, text="7", padx=40, pady=20,command=lambda: click(7))
num8 = Button(window, text="8", padx=40, pady=20,command=lambda: click(8))
num9 = Button(window, text="9", padx=40, pady=20,command=lambda: click(9))
num0 = Button(window, text="0", padx=40, pady=20,command=lambda: click(0))
plus = Button(window, text="+", padx=35, pady=20,command=add)
equal = Button(window, text="=", padx=40, pady=20,command=equal)
clear = Button(window, text="clr", padx=40, pady=20,command=clear)

command=num1.grid(row=1,column=0)
num2.grid(row=1,column=1)
num3.grid(row=1,column=2)
num4.grid(row=2,column=0)
num5.grid(row=2,column=1)
num6.grid(row=2,column=2)
num7.grid(row=3,column=0)
num8.grid(row=3,column=1)
num9.grid(row=3,column=2)
num0.grid(row=4,column=1)
plus.grid(row=5, column=0)
equal.grid(row=6, column=0)
clear.grid(row=6, column=1)
window.mainloop()