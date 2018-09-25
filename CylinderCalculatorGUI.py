import tkinter as tk 

root = tk.Tk() 
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit")
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE )
output.config(state="disabled")
output.pack()
#Event driven programming. The program sits and waits here
#until the user does something like click a button 
root.mainloop() #sets your program in an infinite loop waiting for hte user to do something
				#the program won't go on until you close the window




print("program end")