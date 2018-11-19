#This imports the tkinter "tool box" this contains 
#all the support material to make GUI elements 
#by including "as tk" we are giving a short name to use
import tkinter as tk 


#Main Window 
root = tk.Tk()

#Three stages to build elements/objects
#1. Construct the Object: We build and configure it. 
#2. Configure the Object: We specify behaviours and settings (OPTIONAL)
#3. Pack the Object : Put it in the window 
output = tk.Text(root,height = 10, width = 30) #Parameters are what we send 
#ordered parametrs: The order we send them matters. (C0MMON)
#named parameters: JavaScript and Python specific 
output.config(state = "disable", background = "blue")
output.grid(row = 0, column = 0, rowspan = 5)



  

labInput1 = tk.Label(root, text = "Input 1")
labInput1.grid(row = 5, column = 0)

labInput2 = tk.Label(root, text = "Input 2")
labInput2.grid(row = 6, column = 0)

labInput3 = tk.Label(root, text = "Input 3")
labInput3.grid(row = 7, column = 0)

var1 = tk.IntVar()
var2 = tk.IntVar()

#What the name parameter variable does is binds the INtVar to the 
#checkbox. If there is a change in the box, there is a change in the 
#variable. this is called Binding 

cHC = tk.Checkbutton(root, text="Expand", variable=var1)
cHC.grid(row = 0, column = 1)

cLF = tk.Checkbutton(root, text="Expand", variable=var2)
cLF.grid(row =1, column = 1)

#We are writing an EVENT DRIVE PROGRAM. 
#BUILD THE GUI
#Start it running
#Wait for "EVENT"
root.mainloop()