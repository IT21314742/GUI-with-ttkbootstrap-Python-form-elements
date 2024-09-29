from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = tk()
root.title("TTK Bootstrap!")
# root.iconbitmap('images/codemy.ico')
root.geometry('800x550')

def checker():
    if var1.get() == 1:
        my_label.config(text="Checked!")
    else:
        my_label.config(text="Unchecked!")


# Label
my_label = tb.Label(root, text="Click the checkbox below if you are not robot", font=("Poppins", 15))
my_label.pack(pady=(40,10))

# CheckButton
var1 = IntVar()
my_check = tb.Checkbutton(bootstyle="primary", text="Check Me Out!", variable=var1, onvalue=1, offvalue=0, command=checker )
my_check.pack(pady=10)

# Round ToolButton
var2 = IntVar()
my_check2 = tb.Checkbutton(bootstyle="danger, toolbutton", text="toolButton!!", variable=var2, onvalue=1, offvalue=0, command=checker)
my_check2.pack(pady=10)

# Round ToolButton
var2 = IntVar()
my_check2 = tb.Checkbutton(bootstyle="danger, toolbutton", text="toolButton!!", variable=var2, onvalue=1, offvalue=0, command=checker)
my_check2.pack(pady=10)





# Square Toggle Button



root.mainloop()