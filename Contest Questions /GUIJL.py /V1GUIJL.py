import tkinter as tk 

root = tk.Tk()

label = tk.Label(root, text = "Running Fun",)
label.config(width = 20, height = 10,)
label.grid(row = 0, column = 0, sticky = "w")


label = tk.Label(root, text = "Goal of the Week:")
label.config(width = 20, height = 5)
label.grid(row = 1, column = 0, sticky = "NESW")

Text1 = tk.Entry(root)
Text1.grid(row = 1, column = 1)

Text1 = tk.Entry(root)
Text1.grid(row = 2, column = 1,)

Text1 = tk.Entry(root)
Text1.grid(row = 3, column = 1,)

Text1 = tk.Entry(root)
Text1.grid(row = 4, column = 1,)


label = tk.Label(root, text = "Calories Consumed")
label.config(width = 10, height = 3)
label.grid(row = 2, column = 0, sticky = "NESW")

label = tk.Label(root, text = "Time Slept")
label.config(width = 10, height = 3)
label.grid(row = 3, column = 0, sticky = "NESW")

label = tk.Label(root, text = "Time per min/kilomter")
label.config(width = 20, height = 3)
label.grid(row = 4, column = 0, sticky = "NESW")

root.mainloop()

