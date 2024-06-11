from tkinter import *
import tkinter.messagebox

"======================================= setting ===================================="
root = Tk()
root.title("calculator")
root.geometry("400x200")
color = "gray"
root.configure(bg=color)
root.resizable(width=False ,height=False)

"======================================= variables ===================================="
num_1 = StringVar()
num_2 = StringVar()
res_value = StringVar()

"======================================= functinolity ===================================="
def error_msg(ms):
    if ms == "error":
        tkinter.messagebox.showerror('error','something went error')
    elif ms=="division zero error" :
        tkinter.messagebox.showerror('division error','can not divide by zero')

def plus():
    try:
        value_num_1 = float(num_1.get()) + float(num_2.get())
        res_value.set(value_num_1)
    except:
        error_msg("error")


def minus():
    try:
        value_num_2 = float(num_1.get()) - float(num_2.get())
        res_value.set(value_num_2)
    except:
        error_msg("error")
def mul():
    try:
        value_num_1 = float(num_1.get()) * float(num_2.get())
        res_value.set(value_num_1)
    except:
        error_msg("error")
def div():
    if num_2.get() !='0':
        try:
            value_num_1 = float(num_1.get()) / float(num_2.get())
            res_value.set(value_num_1)
        except:
            error_msg("error")
    elif num_2.get()=='0':
        error_msg("division zero error")
"======================================== frame ===================================="

frame_first = Frame(root,width=400,height=50,bg=color)
frame_first.pack(side=TOP)

frame_second = Frame(root,width=400,height=50,bg=color)
frame_second.pack(side=TOP)

frame_third = Frame(root,width=400,height=50,bg=color)
frame_third.pack(side=TOP)

frame_forth = Frame(root,width=400,height=50,bg=color)
frame_forth.pack(side=TOP)

"======================================= BUTTONS ===================================="
btn_plus = Button(frame_third,text="+",width=10,highlightbackground=color,command=lambda :plus())
btn_plus.pack(side=LEFT,padx=10,pady=10)

btn_minus = Button(frame_third,text="-",width=10,highlightbackground=color,command=lambda :minus())
btn_minus.pack(side=LEFT,padx=10,pady=10)

btn_mul = Button(frame_third,text="*",width=10,highlightbackground=color,command=lambda :mul())
btn_mul.pack(side=LEFT,padx=10,pady=10)

btn_div = Button(frame_third,text="/",width=10,highlightbackground=color,command=lambda :div())
btn_div.pack(side=LEFT,padx=10,pady=10)

"======================================= entries and labels ===================================="
label_first_num= Label(frame_first,text="input number 1 : ",bg=color)
label_first_num.pack(side=LEFT,pady=10,padx=10)

first_num = Entry(frame_first,highlightbackground=color,textvariable=num_1)
first_num.pack(side=LEFT)

label_second_num= Label(frame_second,text="input number 2 : ",bg=color)
label_second_num.pack(side=LEFT,pady=10,padx=10)

second_num = Entry(frame_second,highlightbackground=color,textvariable=num_2)
second_num.pack(side=LEFT)

label_res= Label(frame_forth,text="result : ",bg=color)
label_res.pack(side=LEFT,pady=10,padx=10)

res_num = Entry(frame_forth,highlightbackground=color,textvariable=res_value)
res_num.pack(side=LEFT)


root.mainloop()