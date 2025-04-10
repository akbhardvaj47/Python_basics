from tkinter import *
import math as m

#window configuration
window = Tk()
window.geometry("383x570+470+20")
window.title("cal")
window.config(bg="gray11")
window.resizable(True, False)
window.overrideredirect(1)

#Functions
def close():
    window.destroy()
    
def clear():
    entry.delete(0, "end")
    
def back():
    last_num=len(entry.get())-1
    entry.delete(last_num)
    
'''can be use as
def back():
    entry.delete(len(entry.get()) - 1)'''
    
def press(input):
    length=len(entry.get())
    entry.insert(length, input)

    
def add(a,b):
    return float(a)+float(b)

def subtract(a,b):
    return float(a)-float(b)

def multiply(a,b):
    return float(a)*float(b)

def divide(a, b):
    if b != 0:
        return float(a) / float(b)
    else:
        return "Error: Division by zero"

def expression_break(sign, expression):
    values=expression_break.split(sign,1)
    return values

def scientific(expression):
    data = expression.split("(")[0]
    value = float(expression.split("(")[1].replace(")", ""))
    
    if data == "tan":
        return m.tan(value)
    elif data == "cos":
        return m.cos(value)
    elif data == "sin":
        return m.sin(value)
    elif data == "sqrt":
        return m.sqrt(value)
    elif data == "log":
        return m.log10(value)
    elif data == "ln":
        return m.log(value)
    elif data == "deg":
        return m.degrees(value)
    elif data == "rad":
        return m.radians(value)
    elif data == "fac":
        return m.factorial(int(value))

def equal():
    expression = entry.get()
    clear()
    
    try:
        if "(" in expression:
            result = scientific(expression)
        elif "pow" in expression:
            data = expression.split("pow")
            result = m.pow(float(data[0]), float(data[1]))
        elif "rem" in expression:
            data = expression.split("rem")
            result = float(data[0]) % float(data[1])
        elif "x" in expression or "×" in expression:
            data = expression.replace("x", "*").replace("×", "*").split("*")
            result = multiply(data[0], data[1])
        elif "/" in expression or "÷" in expression:
            data = expression.replace("/", "").replace("÷", "").split("")
            result = divide(data[0], data[1])
        elif "+" in expression:
            data = expression.split("+")
            result = add(data[0], data[1])
        elif "-" in expression:
            data = expression.split("-")
            result = subtract(data[0], data[1])
        
        entry.insert(0, result)
    except Exception as e:
        entry.insert(0, "Error")

            
#Entry Field
entry_string = StringVar()
entry = Entry(window, textvariable = entry_string, foreground="white",
              background="gray20", border=0, font=("bahnschrift Semibold",26))
entry.grid(columnspan=4, ipady=15)
font_value = ("calibary", 18)

#Buttons
btn_tan = Button(window, text="tan", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("tan("))
btn_tan.grid(row=1, column=0, sticky=E+W, ipady=5)

btn_cos = Button(window, text="cos", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("cos("))
btn_cos.grid(row=1, column=1, sticky=E+W, ipady=5)

btn_sin = Button(window, text="sin", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("sin("))
btn_sin.grid(row=1, column=2, sticky=E+W, ipady=5)

btn_sqrt = Button(window, text="sqrt", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID,  command=lambda:press("sqrt("))
btn_sqrt.grid(row=1, column=3, sticky=E+W, ipady=5)




btn_log = Button(window, text="log", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID,  command=lambda:press("log("))
btn_log.grid(row=2, column=0, sticky=E+W, ipady=5)

btn_ln = Button(window, text="ln", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID,  command=lambda:press("ln("))
btn_ln.grid(row=2, column=1, sticky=E+W, ipady=5)

btn_deg = Button(window, text="deg", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("deg("))
btn_deg.grid(row=2, column=2, sticky=E+W, ipady=5)

btn_rad = Button(window, text="rad", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("rad("))
btn_rad.grid(row=2, column=3, sticky=E+W, ipady=5)





btn_fac = Button(window, text="fac", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID,  command=lambda:press("fac("))
btn_fac.grid(row=3, column=0, sticky=E+W, ipady=5)

btn_pow = Button(window, text="pow", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("pow"))
btn_pow.grid(row=3, column=1, sticky=E+W, ipady=5)

btn_rem = Button(window, text="rem", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("rem"))
btn_rem.grid(row=3, column=2, sticky=E+W, ipady=5)

btn_pi = Button(window, text="pi", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(3.14))
btn_pi.grid(row=3, column=3, sticky=E+W, ipady=5)



btn_clear = Button(window, text="C", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command = clear)
btn_clear.grid(row=4,columnspan=2, column=0, sticky=E+W, ipady=5)

btn_backspace = Button(window, text="X", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command = back)
btn_backspace.grid(row=4,columnspan=2, column=2, sticky=E+W, ipady=5)


btn_7 = Button(window, text="7", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(7))
btn_7.grid(row=5, column=0, sticky=E+W, ipady=5)

btn_8 = Button(window, text="8", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(8))
btn_8.grid(row=5, column=1, sticky=E+W, ipady=5)

btn_9 = Button(window, text="9", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(9))
btn_9.grid(row=5, column=2, sticky=E+W, ipady=5)

btn_add = Button(window, text="+", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("+"))
btn_add.grid(row=5, column=3, sticky=E+W, ipady=5)


btn_4 = Button(window, text="4", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(4))
btn_4.grid(row=6, column=0, sticky=E+W, ipady=5)

btn_5 = Button(window, text="5", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(5))
btn_5.grid(row=6, column=1, sticky=E+W, ipady=5)

btn_6 = Button(window, text="6", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(6))
btn_6.grid(row=6, column=2, sticky=E+W, ipady=5)

btn_sub = Button(window, text="-", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("-"))
btn_sub.grid(row=6, column=3, sticky=E+W, ipady=5)




btn_1 = Button(window, text="1", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(1))
btn_1.grid(row=7, column=0, sticky=E+W, ipady=5)

btn_2 = Button(window, text="2", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(2))
btn_2.grid(row=7, column=1, sticky=E+W, ipady=5)

btn_3 = Button(window, text="3", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(3))
btn_3.grid(row=7, column=2, sticky=E+W, ipady=5)

btn_mul = Button(window, text="*", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("*"))
btn_mul.grid(row=7, column=3, sticky=E+W, ipady=5)




btn_dot = Button(window, text=".", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("."))
btn_dot.grid(row=8, column=0, sticky=E+W, ipady=5)

btn_0 = Button(window, text="0", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(0))
btn_0.grid(row=8, column=1, sticky=E+W, ipady=5)

btn_e = Button(window, text="e", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press(3.1645))
btn_e.grid(row=8, column=2, sticky=E+W, ipady=5)

btn_div = Button(window, text="/", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command=lambda:press("/"))
btn_div.grid(row=8, column=3, sticky=E+W, ipady=5)



btn_equal = Button(window, text="=", background="orange",
                 foreground="white", font=font_value, borderwidth=1,
                 relief=SOLID,command=equal)
btn_equal.grid(row=9,columnspan=3, column=0, sticky=E+W, ipady=5)


btn_close = Button(window, text="close", background="gray11",
                 foreground="DarkOrange1", font=font_value, borderwidth=1,
                 relief=SOLID, command = close)
btn_close.grid(row=9, column=3, sticky=E+W, ipady=5)












