import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text = "Grid", font = ("comic sans",20))
label.grid(row = 0, column = 0, columnspan = 2)

btn1 = tk.Button(root, text = "oof")
btn1.grid(row = 1, column = 0, sticky = "NESW")
btn1.config(width = 10, height = 5)

btn2 = tk.Button(root, text = "oof")
btn2.grid(row = 2, column = 0, sticky = "NESW")
btn2.config(width = 10, height = 5)

btn3 = tk.Button(root, text = "oof")
btn3.grid(row = 3, column = 0, sticky = "NESW")
btn3.config(width = 10, height = 5)

btn4 = tk.Button(root, text = "oof")
btn4.grid(row = 4, column = 0, sticky = "NESW")
btn4.config(width = 10, height = 5)

root.mainloop()