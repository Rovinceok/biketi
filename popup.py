import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Pop-up Notification Demo")

# Create a function to display the pop-up notification
def show_notification():
    messagebox.showinfo("Notification", "Order placed successfully. Thank you!")

# Create a button and add it to the main window
button = tk.Button(root, text="Place your order", command=show_notification)
button.pack(padx=20, pady=20)

# Start the main event loop
root.mainloop()
