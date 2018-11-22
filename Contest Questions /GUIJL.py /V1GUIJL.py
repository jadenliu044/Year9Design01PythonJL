import tkinter as tk 

root = tk.Tk()

label = tk.Label(root, text = "Goal of the Week")
label.config(width = 20, height = 5)
label.grid(row = 0, column = 0, sticky = "E")

btn1 = tk.Button(root, text = "Calories Consumed")
btn1.config(width = 5, height = 5)
btn1.grid(row = 1, column = 0, sticky = "NESW")

btn2 = tk.Button(root, text = )

root.mainloop()