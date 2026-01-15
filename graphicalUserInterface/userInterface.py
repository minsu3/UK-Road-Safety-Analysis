print("Script started")

import tkinter as tk

root = tk.Tk()
root.title("Hello World App")
root.geometry("300x150")

label = tk.Label(root, text="Hello world!", font=("Helvetica", 16))
label.pack(pady=50)

root.mainloop()