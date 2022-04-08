from tkinter import *

def btn(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def clear():
    global operator
    operator = ''
    text_input.set('')
    screen.insert(0, '0')

def Equal():
    global operator
    sumup = float(eval(operator))
    text_input.set(sumup)
    operator=''

root = Tk()
root.title('Calculator')
root.geometry('340x480')

operator = ''
text_input = StringVar(value = '0')

#============================ Screen===============================
screen = Entry(font = ('arial', 20, 'bold'), fg='black', bg='white', bd=20, justify='right', textvariable=text_input)
screen.grid(row=0, columnspan=4)

#=========================== Row1==================================

btn1 = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='1', bg='white', fg= 'black', bd = 8, command = lambda:btn(1)).grid(row=1, column=0)
btn2 = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='2', bg='white', fg= 'black', bd = 8, command = lambda:btn(2)).grid(row=1, column=1)
btn3 = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='3', bg='white', fg= 'black', bd = 8, command = lambda:btn(3)).grid(row=1, column=2)
btnclear = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='C', bg='green', fg= 'black', bd = 8, command = clear).grid(row=1, column=3)

#============================Row2==================================

btn4 = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='4', bg='white', fg= 'black', bd = 8, command = lambda:btn(4)).grid(row=2, column=0)
btn5 = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='5', bg='white', fg= 'black', bd = 8, command = lambda:btn(5)).grid(row=2, column=1)
btn6 = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='6', bg='white', fg= 'black', bd = 8, command = lambda:btn(6)).grid(row=2, column=2)
btnplus = Button(root, padx = 21, pady = 15, font = ('arial', 15, 'bold'), text ='+', bg='yellow', fg= 'black', bd = 8, command = lambda:btn('+')).grid(row=2, column=3)

#============================Row3==================================

btn7 = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='7', bg='white', fg= 'black', bd = 8, command = lambda:btn(7)).grid(row=3, column=0)
btn8 = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='8', bg='white', fg= 'black', bd = 8, command = lambda:btn(8)).grid(row=3, column=1)
btn9 = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='9', bg='white', fg= 'black', bd = 8, command = lambda:btn(9)).grid(row=3, column=2)
btnminus = Button(root, padx = 23, pady = 15, font = ('arial', 15, 'bold'), text ='-', bg='yellow', fg= 'black', bd = 8, command = lambda:btn('-')).grid(row=3, column=3)

#============================Row4==================================

btn0 = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='0', bg='white', fg= 'black', bd = 8, command = lambda:btn(0)).grid(row=4, column=0)
btndiv = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='/', bg='yellow', fg= 'black', bd = 8, command = lambda:btn('/')).grid(row=4, column=1)
btnmul = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='*', bg='yellow', fg= 'black', bd = 8, command = lambda:btn('*')).grid(row=4, column=2)
btndot = Button(root, padx = 24, pady = 15, font = ('arial', 15, 'bold'), text ='.', bg='yellow', fg= 'black', bd = 8, command = lambda:btn('.')).grid(row=4, column=3)
#btn13 = Button(text='Close', command = root.destroy()).grid()

#============================Row4==================================
btnequal = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='=', bg='green', fg= 'black', bd = 8, command = Equal).grid(row=5, column=0)
btnopenbracket = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text ='(', bg='yellow', fg= 'black', bd = 8, command = lambda:btn('(')).grid(row=5, column=1)
btnclosebracket = Button(root, padx = 20, pady = 15, font = ('arial', 15, 'bold'), text =')', bg='yellow', fg= 'black', bd = 8, command = lambda:btn(')')).grid(row=5, column=2)
btncsquare = Button(root, padx = 21, pady = 15, font = ('arial', 15, 'bold'), text ='^', bg='yellow', fg= 'black', bd = 8, command = lambda:btn('**')).grid(row=5, column=3)

root.mainloop()