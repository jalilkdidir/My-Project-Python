from tkinter import *


exprission = ''

def press(userInput):
    global exprission
    exprission = exprission + str(userInput)
    equation.set(exprission)

def equalPress():
    try:

        global exprission
        result = str(eval(exprission))
        equation.set(result)
        exprission = ''
    except:
        exprission.__setattr__('error')


def clear():
    global exprission
    exprission = ''
    equation.set('')

root = Tk()
root.geometry('280x250')
root.resizable(False,False)
equation = StringVar()

lbl = Label(root,text='Simpl Calculater',font=('helvitica 20 bold'),fg='red')
lbl.grid(columnspan=4)

ent = Entry(root,textvariable=equation)
ent.grid(columnspan=4, padx=5 ,pady=10,ipadx=74,ipady=7)

btn1 = Button(root, text=' 1 ',height=1,command=lambda :press(1) ,width=7,font=('helvitica 10 bold'),fg='red')
btn1.grid(row=2 , column=0)
btn2 = Button(root, text=' 2 ',height=1,command=lambda :press(2) ,width=7,font=('helvitica 10 bold'),fg='red')
btn2.grid(row=2 , column=1)
btn3 = Button(root, text=' 3 ',height=1,command=lambda :press(3) ,width=7,font=('helvitica 10 bold'),fg='red')
btn3.grid(row=2 , column=2)
btn4 = Button(root, text=' 4 ',height=1,command=lambda :press(4) ,width=7,font=('helvitica 10 bold'),fg='red')
btn4.grid(row=3 , column=0)
btn5 = Button(root, text=' 5 ',height=1,command=lambda :press(5) ,width=7,font=('helvitica 10 bold'),fg='red')
btn5.grid(row=3 , column=1)
btn6 = Button(root, text=' 6 ',height=1,command=lambda :press(6) ,width=7,font=('helvitica 10 bold'),fg='red')
btn6.grid(row=3 , column=2)
btn7 = Button(root, text=' 7 ',height=1,command=lambda :press(7) ,width=7,font=('helvitica 10 bold'),fg='red')
btn7.grid(row=4 , column=0)
btn8 = Button(root, text=' 8 ',height=1,command=lambda :press(8) ,width=7,font=('helvitica 10 bold'),fg='red')
btn8.grid(row=4 , column=1)
btn9 = Button(root, text=' 9 ',height=1,command=lambda :press(9) ,width=7,font=('helvitica 10 bold'),fg='red')
btn9.grid(row=4 , column=2)
btnplus = Button(root, text=' + ',height=1,command=lambda :press('+') ,width=7,font=('helvitica 10 bold'),fg='red')
btnplus.grid(row=2 , column=3)
btnmin = Button(root, text=' - ',height=1,command=lambda :press('-') ,width=7,font=('helvitica 10 bold'),fg='red')
btnmin.grid(row=3 , column=3)
btnmult = Button(root, text=' x ',height=1,command=lambda :press('*') ,width=7,font=('helvitica 10 bold'),fg='red')
btnmult.grid(row=4 , column=3)
btndef = Button(root, text=' % ',height=1,command=lambda :press('%') ,width=7,font=('helvitica 10 bold'),fg='red')
btndef.grid(row=5 , column=3)
btnecua = Button(root, text=' = ',height=1,command=equalPress ,width=7,fg='white' ,bg='green')
btnecua.grid(row=5 , column=2)
btnclear = Button(root, text=' C ',height=1,command=clear ,width=7,bg='red')
btnclear.grid(row=6 , column=0)
btnclear = Button(root, text=' . ',height=1,command=lambda :press('.') ,width=7,font=('helvitica 10 bold'),fg='red')
btnclear.grid(row=5 , column=0)
btnclear = Button(root, text=' 0 ',height=1,command=lambda :press(0) ,width=7,font=('helvitica 10 bold'),fg='red')
btnclear.grid(row=5 , column=1)

root.mainloop()