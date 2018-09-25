import tkinter as tk

def sumbit():

	print("Submit pressed")
	r = float(entr.get())
	h = float(enth.get())

	output.config(state="normal")
	output.insert(tk.INSERT,v)
	output.config(state="disabled")

v = math.pi*r*r*h
v = round(v,3)

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

btn = tk.Button(root, text="submit", command=submit)
btn.pack()

output = tk.Text(root, width=100, height=100, borderwidth=50, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

root.mainloop()