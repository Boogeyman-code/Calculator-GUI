import tkinter as tk


#---------------------Display----------------#

root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
root.configure(bg="#1e1e1e")
root.resizable(False,False)

expression = ""
equation = tk.StringVar()


#---------------------Functions----------------#

def press(num):
    global expression

    expression +=str(num)
    equation.set(expression)

def equal():
    global expression

    try:
        result=str(eval(expression))
        equation.set(result)

    except ZeroDivisionError:
        equation.set("Cannot Divide by 0")
        expression = ""

    except:
        equation.set("Error")
        expression =""

def clear():
    global expression

    expression =""
    equation.set("")

def backspace():
    global expression

    expression = expression[:-1]
    equation.set(expression)

#---------------------Display----------------#

entry = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial",28),
    bd=10,
    relief=tk.FLAT,
    justify="right",
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)

entry.grid(
    row=0,
    column=0,
    columnspan=4,
    ipadx=8,
    ipady=25,
    padx=10,
    pady=20,
    sticky="nsew"
)


#---------------------Style----------------#

btn_style = {
    "font": ("Arial", 18, "bold"),
    "width":5,
    "height":2,
    "bg":"#333333",
    "fg":"white",
    "activebackground":"#555555",
    "relief":tk.FLAT
}


#---------------------Buttons----------------#

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text,row,col) in buttons:

    if text == "=":
        button=tk.Button(
            root,
            text=text,
            command=equal,
            bg="green",
            fg="white",
            font=("Arial", 18, "bold"),
            width=5,
            height=2,
            relief=tk.FLAT
        )

    else:
        button = tk.Button(
            root,
            text=text,
            command=lambda t=text: press(t),
            **btn_style
        )
    
    button.grid(
        row=row,
        column=col,
        padx=5,
        pady=5,
        sticky="nsew"
    )

#---------------------- Extra Buttons----------------#

clear_btn = tk.Button(
    root,
    text="C",
    command=clear,
    bg="red",
    fg="white",
    font=("Arial", 18, "bold"),
    width=11,
    height=2,
    relief=tk.FLAT
)

clear_btn.grid(
    row=5,
    column=0,
    columnspan=2,
    padx=5,
    pady=5,
    sticky="nsew"
)

back_btn = tk.Button(
    root,
    text="Clear",
    command=backspace,
    bg="orange",
    fg="white",
    font=("Arial", 18, "bold"),
    width=11,
    height=2,
    relief=tk.FLAT
)

back_btn.grid(
    row=5,
    column=2,
    columnspan=2,
    padx=5,
    pady=5,
    sticky="nsew"
)

#-----------------------Response----------------#

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

#-----------------------APP------------------#
root.mainloop()