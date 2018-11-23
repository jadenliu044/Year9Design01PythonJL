import tkinter as tk 

root = tk.Tk()


label = tk.Label(root, text = "Goal of the Week:")
label.config(width = 20, height = 5)
label.grid(row = 0, column = 0, sticky = "E")

btn1 = tk.Button(root, text = "Calories Consumed")
btn1.config(width = 10, height = 5)
btn1.grid(row = 1, column = 0, sticky = "NESW")

btn2 = tk.Button(root, text = "Time Slept")
btn2.config(width = 10, height = 5)
btn2.grid(row = 1, column = 1, sticky = "NESW")

btn3 = tk.Button(root, text = "Time per min/kilomter")
btn3.config(width = 15, height = 5)
btn3.grid(row = 2, column = 0, sticky = "E")


root.mainloop()