from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = tk()
root.title("TTK Bootstrap!")
# root.iconbitmap('images/codemy.ico')
root.geometry('800x550')

def fname(arg):
    pass


# Label
my_label = tb.Label(root, text="Click the checkbox below if you are not robot", font=("Poppins", 15))
my_label.pack(pady=(40,10))

# CheckButton
var1 = IntVar()
my_check = tb.Checkbutton(bootstyle="primary", text="Check Me Out!", variable=var1, onvalue=1, offvalue=0, command=checker )
my_check.pack(pady=10)

# Round Toggle Button

# Square Toggle Button



root.mainloop()