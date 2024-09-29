from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = tk()
root.title("TTK Bootstrap!")
# root.iconbitmap('images/codemy.ico')
root.geometry('500x350')


# Label
my_label = tb.Label(root, text="Click the checkbox below if you are not robot", font=("Poppins", 20))
my_label.pack(pady=(40,10))

# CheckButton

# Round Toggle Button

# Square Toggle Button



root.mainloop()