import tkinter as tk
from tkinter import ttk
from os import name
win= tk.Tk()
win.title('Python GUI')
win.resizable(500,500)
label=ttk.Label(win,text='A label')
label.grid(column=0,row=0)




def clickMe():
    action.configure(text="** I have been clicked! **" + name.get())
    label.configure(foreground="red")

    action=ttk.Button(win,text="ClickMe",command="clickMe")
    action.grid(column=1,row=1)
win.mainloop()
