import tkinter as tk
import math

def sumbit():

	print("Submit pressed")
	r = float(entr.get())
	h = float(enth.get())

	output.config(state="normal")

	outputValue = "Given\nradius:"+str(r)" units\nheight:"+str(h)+" units\nThe volume is:"+str(v)+" units cubed\n"

	output.insert(tk.INSERT,outputValue)
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