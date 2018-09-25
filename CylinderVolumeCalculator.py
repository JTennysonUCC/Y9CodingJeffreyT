import tkinter as tk

root = tk.Tk()
root.title("volume of a cylinder")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="submit")
btn.pack()

output = tk.Text(root, width=100, height=100, borderwidth=50, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

root.mainloop()