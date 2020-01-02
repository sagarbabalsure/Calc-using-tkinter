from tkinter import *

window=Tk()
window.title("Calculator")
window.geometry("250x345")
window.resizable(0,0)

tinput=StringVar()
operator=""

def click_on_button(number):
	global operator
	operator=operator+str(number)
	tinput.set(operator)

def equal():
	global operator
	add=str(eval(operator))
	tinput.set(add)
	operator=""
def equal():
	global operator
	sub=str(eval(operator))
	tinput.set(sub)
	operator=""
def equal():
	global operator
	mul=str(eval(operator))
	tinput.set(mul)
	operator=""
def equal():
	global operator
	div=str(eval(operator))
	tinput.set(div)
	operator=""
	
def clear():
	global operator
	operator=""
	tinput.set(operator)

def back():
	tinput.set(operator[:-1])



frame1=Frame(window)
frame1.pack(side=TOP)
label_1=Label(window,text="Calculator",bg="Dark grey",font=("Arial",20,"bold")).pack()
e1=Entry(window,bg="yellow",width=30,textvariable=tinput)
e1.pack()
frame2=Frame(window)
frame2.pack(side=BOTTOM)

b_equal=Button(window,text="=",height=2,width=12,command=equal)
b_equal.place(x=0,y=60)
b_calcel=Button(window,text="Back",height=2,width=12,command=back)
b_calcel.place(x=124,y=60)
b1=Button(window,text="1",height=3,width=4,command=lambda:click_on_button(1))
b1.place(x=0,y=100)
b2=Button(window,text="2",height=3,width=4,command=lambda:click_on_button(2))
b2.place(x=62,y=100)
b3=Button(window,text="3",height=3,width=4,command=lambda:click_on_button(3))
b3.place(x=124,y=100)
b_plus=Button(window,text="+",height=3,width=4,command=lambda:click_on_button("+"))
b_plus.place(x=186,y=100)
b4=Button(window,text="4",height=3,width=4,command=lambda:click_on_button(4))
b4.place(x=0,y=160)
b5=Button(window,text="5",height=3,width=4,command=lambda:click_on_button(5))
b5.place(x=62,y=160)
b6=Button(window,text="6",height=3,width=4,command=lambda:click_on_button(5))
b6.place(x=124,y=160)
b_minus=Button(window,text="-",height=3,width=4,command=lambda:click_on_button("-"))
b_minus.place(x=186,y=160)
b7=Button(window,text="7",height=3,width=4,command=lambda:click_on_button(7))
b7.place(x=0,y=220)
b8=Button(window,text="8",height=3,width=4,command=lambda:click_on_button(8))
b8.place(x=62,y=220)
b9=Button(window,text="9",height=3,width=4,command=lambda:click_on_button(9))
b9.place(x=124,y=220)
b_mul=Button(window,text="*",height=3,width=4,command=lambda:click_on_button("*"))
b_mul.place(x=186,y=220)
b0=Button(window,text="0",height=3,width=4,command=lambda:click_on_button(0))
b0.place(x=0,y=280)
b_point=Button(window,text=".",height=3,width=4,command=lambda:click_on_button("."))
b_point.place(x=62,y=280)
b_clear=Button(window,text="c",height=3,width=4,command=clear)
b_clear.place(x=124,y=280)
b_div=Button(window,text="/",height=3,width=4,command=lambda:click_on_button("/"))
b_div.place(x=186,y=280)


window.mainloop()