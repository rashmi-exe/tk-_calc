from tkinter import *
import math
root = Tk()
root.title("simple calculator")
root.iconbitmap(r"D:\python\GUI\img\favicon.ico")
# use lambda to pass parameters in functions
# e.delete(0,END) deleltes all the content in the field
e = Entry(root, width=30, borderwidth=10,)  # input field
# label below the input field to show the operation going on
mylabel = Label(root, text=" ", width=30, fg="gray")

# function to update the input fields


def myClick(num):
    curr = e.get()  # to store the data which is already entered in the input field
    e.delete(0, END)  # delete the existing data
    e.insert(0, str(curr)+str(num))  # conactenate the previous and new data
# def myClickdec()

# function for clear button


def clearbtn():
    e.delete(0, END)
    mylabel.config(text=" ")

# function for add button


def add_btn():
    prev = e.get()  # get the previous number entered
    global f_num  # since we cant return a value from the function we declared it as global so that we can use it elsewhere
    f_num = prev
    if (signval == "neg"):
        f_num = prev*-1
    # clear the input field so that the user can type the second number
    e.delete(0, END)
    mylabel.config(text=str(prev)+"+")  # display the operation in the label

    # f_num = 0

# function for add button


def sub_btn():
    prev = e.get()  # get the previous number entered
    global f_num   # both btns cant be used at the same time so we can declare it twice
    f_num = prev
    # clear the input field so that the user can type the second number
    e.delete(0, END)
    mylabel.config(text=str(prev)+"-")  # display the operation in the label


def multiply_btn():
    prev = e.get()  # get the previous number entered
    global f_num   # both btns cant be used at the same time so we can declare it twice
    f_num = prev
    # clear the input field so that the user can type the second number
    e.delete(0, END)
    mylabel.config(text=str(prev)+"*")  # display the operation in the label


def divide_btn():
    prev = e.get()  # get the previous number entered
    global f_num   # both btns cant be used at the same time so we can declare it twice
    f_num = prev
    # clear the input field so that the user can type the second number
    e.delete(0, END)
    mylabel.config(text=str(prev)+"/")  # display the operation in the label


def sign_btn():
    global signval
    signval = "neg"
    e.delete(0, END)
    mylabel.config(text="-"+str(prev))  # display the operation in the label
# function for equal button


def power_btn():
    prev = e.get()  # get the previous number entered
    global f_num   # both btns cant be used at the same time so we can declare it twice
    f_num = prev
    # clear the input field so that the user can type the second number
    e.delete(0, END)
    mylabel.config(text=str(prev)+"^")  # display the operation in the label


def equal_btn():
    new = e.get()  # get the second number number entered
    e.delete(0, END)  # clear the input field
    t = mylabel.cget("text")  # get the exsiting text in mylabel
    if (t[-1] == "+"):  # if t as + end then perform addition
        result = float(f_num)+float(new)
    elif (t[-1] == "-"):  # if t as - end then perform subtraction
        result = int(f_num)-int(new)
    elif (t[-1] == "*"):  # if t as * end then perform multiplication
        result = int(f_num)*int(new)
    elif (t[-1] == "/"):  # if t as / end then perform divison
        result = int(f_num)/int(new)
    elif (t[-1] == "^"):  # if t as / end then perform power
        result = math.pow(float(f_num), float(new))
    elif (t[0] == "-"):  # if t as / end then perform divison
        result = "-"+str(new)
    else:  # if none then display what is there in the input field
        result = new
    e.insert(0, str(result))
    mylabel.config(text=str(result))


# define all buttons
button_1 = Button(root, text="1", padx=10, pady=10,
                  borderwidth=2, bg="white", fg="black", command=lambda: myClick(1))
button_2 = Button(root, text="2", padx=10, pady=10,
                  borderwidth=2, bg="white", fg="black", command=lambda: myClick(2))
button_3 = Button(root, text="3", padx=10, pady=10,
                  borderwidth=2, bg="white", fg="black", command=lambda: myClick(3))
button_4 = Button(root, text="4", padx=10, pady=10,
                  borderwidth=2, bg="white", fg="black", command=lambda: myClick(4))
button_5 = Button(root, text="5", padx=10, pady=10,
                  borderwidth=2, bg="white", fg="black", command=lambda: myClick(5))
button_6 = Button(root, text="6", padx=10, pady=10,
                  borderwidth=2, bg="white", fg="black", command=lambda: myClick(6))
button_7 = Button(root, text="7", padx=10, pady=10,
                  borderwidth=2, bg="white", fg="black", command=lambda: myClick(7))
button_8 = Button(root, text="8", padx=10, pady=10,
                  borderwidth=2, bg="white", fg="black", command=lambda: myClick(8))
button_9 = Button(root, text="9", padx=10, pady=10,
                  borderwidth=2, bg="white", fg="black", command=lambda: myClick(9))
button_0 = Button(root, text="0", padx=10, pady=10,
                  borderwidth=2, bg="white", fg="black", command=lambda: myClick(0))
button_dec = Button(root, text=".", padx=10, pady=10,
                    borderwidth=2, bg="white", fg="black", command=lambda: myClick("."))
add = Button(root, text="+", padx=10, pady=10,
             borderwidth=8, fg='blue', command=add_btn)
sub = Button(root, text="-", padx=10, pady=10,
             borderwidth=8, fg='blue', command=sub_btn)
multiply = Button(root, text="*", padx=10, pady=10,
                  borderwidth=8, fg='blue', command=multiply_btn)
divide = Button(root, text="/", padx=10, pady=10,
                borderwidth=8, fg='blue', command=divide_btn)
power = Button(root, text="x^y", padx=10, pady=10,
               borderwidth=8, fg='blue', command=power_btn)
sign = Button(root, text="+/-", padx=10, pady=10,
              borderwidth=8, fg='blue', command=sign_btn)
# sq = Button(root, text="", padx=10, pady=10,
#             borderwidth=8, fg='blue', command=sq_btn)
equal = Button(root, text="=", padx=10, pady=10,
               borderwidth=8, fg='blue', command=equal_btn)
clear = Button(root, text="C", padx=10, pady=10,
               borderwidth=8, fg="red", command=clearbtn)
# place the buttons and fields
e.grid(row=0, column=0, columnspan=4, rowspan=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_0.grid(row=6, column=0)
add.grid(row=3, column=3)
sub.grid(row=4, column=3)
multiply.grid(row=5, column=3)
divide.grid(row=6, column=3)
power.grid(row=7, column=0)
button_dec.grid(row=6, column=1)
# divide(row=6, coloumn=3)
equal.grid(row=6, column=2)
clear.grid(row=7, column=1,)
sign.grid(row=7, column=2)
mylabel.grid(row=2, column=0, columnspan=4)

root.mainloop()
