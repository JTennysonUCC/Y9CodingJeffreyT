import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text = "Click the button to test how fast you can click")
label.grid(row = 0, column = 0, columnspan = 2)

btn1 = tk.Button(root, text = "click here")
btn1.grid(row = 1, column = 0, sticky = "NESW")
btn1.config(width = 20, height = 1)

root.mainloop()