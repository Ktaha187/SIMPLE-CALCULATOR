
from tkinter import *
def btnClick(number):
    global operator
    operator=operator+str(number)
    text_input.set(operator)
def btnClear():
    global operator
    operator=" "
    text_input.set(" ")
def btnEqual():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=" "
win=Tk()
win.title("SIMPLE CALCULATOR")
operator=" "
text_input=StringVar()

bisplay_box=Entry(win,font=("verdana",9),textvariable=text_input,bd=20,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)
button7=Button(win,padx=16,pady=10,bd=8,fg="black",text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
button8=Button(win,padx=16,pady=10,bd=8,fg="black",text="8",command=lambda:btnClick(8)).grid(row=1,column=1)
button9=Button(win,padx=16,pady=10,bd=8,fg="black",text="9",command=lambda:btnClick(9)).grid(row=1,column=2)
add=Button(win,padx=16,pady=10,bd=8,fg="black",text="+",command=lambda:btnClick("+")).grid(row=1,column=3)
#==========================================================
bisplay_box=Entry(win,font=("verdana",9),textvariable=text_input,bd=20,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)
button4=Button(win,padx=16,pady=10,bd=8,fg="black",text="4",command=lambda:btnClick(4)).grid(row=2,column=0)
button5=Button(win,padx=16,pady=10,bd=8,fg="black",text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
button6=Button(win,padx=16,pady=10,bd=8,fg="black",text="6",command=lambda:btnClick(6)).grid(row=2,column=2)
sub=Button(win,padx=16,pady=10,bd=8,fg="black",text="-",command=lambda:btnClick("-")).grid(row=2,column=3)
# =================================================================
button1=Button(win,padx=16,pady=10,bd=8,fg="black",text="1",command=lambda:btnClick(1)).grid(row=3,column=0)
button2=Button(win,padx=16,pady=10,bd=8,fg="black",text="2",command=lambda:btnClick(2)).grid(row=3,column=1)
button3=Button(win,padx=16,pady=10,bd=8,fg="black",text="3",command=lambda:btnClick(3)).grid(row=3,column=2)
mul=Button(win,padx=16,pady=10,bd=8,fg="black",text="*",command=lambda:btnClick("*")).grid(row=3,column=3)
#===============================================================
button0=Button(win,padx=16,pady=10,bd=8,fg="black",text="0",command=lambda:btnClick(0)).grid(row=4,column=0)
buttonClear=Button(win,padx=16,pady=10,bd=8,fg="black",text="c",command=btnClear).grid(row=4,column=1)
buttonEquals=Button(win,padx=16,pady=10,bd=8,fg="black",text="=",command=btnEqual).grid(row=4,column=2)
divide=Button(win,padx=16,pady=10,bd=8,fg="black",text="/",command=lambda:btnClick("/")).grid(row=4,column=3)
win.mainloop()


















