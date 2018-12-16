import tkinter as tk 

def submit():

	print("submit")
	#Since you have three pieces of data 
	listcal.append(entcal.get())
	listsleep.append(enttimesleep.get())
	listtpk.append(enttpk.get())

	print(listcal)
	print(listsleep)
	print(listtpk)

	#How many tpk do you need before you can find a difference from the average
	#Check the lenght of tpk
	if len(listtpk) > 0:
		#find the average
		#
		sum = 0 #stores sum
		#Find sum of listtpk
		for i in range(0,len(listtpk),1):
			sum = sum + float(listtpk[i])
			
		#Example listtpk = [2,6,4] 
		# i = 0 | 0 < 3 | T - sum = 0 + listtpk[0] = 0 + 2 = 2
		# i = 1 | 1 < 3 | T - sum = 2 + listtpk[1] = 2 + 6 = 8
		# i = 2 | 2 < 3 | T - sum = 8 + listtpk[2] = 8 + 4 = 12
		# i = 3 | 3 < 3 | F - EXIT LOOP 
		average = sum/len(listtpk)
		print(average)
		timecomp = average - float(enttpk.get())

		labeltcomp.config(text = "Time Comparison versus average run +/- = "+str(average))


	if len(listcal) > 0:
		
		
		sum = 0 
		
		for i in range(0,len(listcal),1):
			sum = sum + float(listcal[i])
		 
		average = sum/len(listcal)
		print(average)
		caloriescomp = average - float(entcal.get())

		labelccomp.config(text = "Difference in Calories Consumed +/- = "+str(average))


		

		

	if len(listsleep) > 0:
		
		
		sum = 0 
		
		for i in range(0,len(listsleep),1):
			sum = sum + float(listsleep[i])
		 
		average = sum/len(listsleep)
		print(average)
		sleepcomp = average - float(enttimesleep.get())

		labelscomp.config(text = "Difference in Time Slept +/- = "+str(average))



		

#Create three parallel lists, store each piece of information
listcal = [] #empty
listsleep = [] #empty
listtpk = [] #empty




root = tk.Tk()





label = tk.Label(root, text = "Today's Run",)
label.config(width = 10, font = ("Arrus BT", 20))
label.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")


labelgoal = tk.Label(root, text = "Goal of the Week:")
labelgoal.config(width = 20, height = 2)
labelgoal.grid(row = 1, column = 0, sticky = "NESW")

entgoal = tk.Entry(root)
entgoal.grid(row = 1, column = 1)

labelcal = tk.Label(root, text = "Calories Consumed")
labelcal.config(width = 20, height = 2)
labelcal.grid(row = 2, column = 0, sticky = "NESW")

entcal = tk.Entry(root)
entcal.grid(row = 2, column = 1,)

labeltimesleep = tk.Label(root, text = "Time Slept - Last Night")
labeltimesleep.config(width = 20, height = 2)
labeltimesleep.grid(row = 3, column = 0, sticky = "NESW")

enttimesleep = tk.Entry(root)
enttimesleep.grid(row = 3, column = 1,)

labeltpk = tk.Label(root, text = "Time per min/kilomter")
labeltpk.config(width = 20, height = 2)
labeltpk.grid(row = 4, column = 0, sticky = "NESW")   

enttpk = tk.Entry(root)
enttpk.grid(row = 4, column = 1,)

btnsubmit = tk.Button(root, text = "submit", command = submit)
btnsubmit.grid(row = 5, column = 0, columnspan = 2)





labelcomp = tk.Label(root, text = "Differences/Comparison versus the average")
labelcomp.config(width = 30, height = 2, font = ("Arrus BT", 20))
labelcomp.grid(row = 6, column = 0, columnspan = 2, sticky = "NESW")

labeltcomp = tk.Label(root, text = "Time Comparison versus average run +/- = ??")
labeltcomp.config(width = 30, height = 2)
labeltcomp.grid(row = 7, column = 0, columnspan = 2, sticky = "NESW")

labeldiffcal = tk.Label(root, text = "Difference in Calories Consumed +/- = ??")
labeldiffcal.config(width = 25, height = 2)
labeldiffcal.grid(row = 8, column = 0, columnspan = 2, sticky = "NESW")


labeldiffsleep = tk.Label(root, text = "Difference in Time Slept +/- = ??")
labeldiffsleep.config(width = 25, height = 2)
labeldiffsleep.grid(row = 9, column = 0, columnspan = 2, sticky = "NESW")


labeldifftime = tk.Label(root, text = "Time per Kilometer +/- = ??")
labeldifftime.config(width = 25, height = 2)
labeldifftime.grid(row = 10, column = 0, sticky = "NESW")

labelgraph = tk.Label(root, text = "GRAPH")
labelgraph.config(width = 10, height = 1, font = ("Arrus BT", 20))
labelgraph.grid(row = 11, column = 0, columnspan = 2, sticky = "NESW")

print("TEST")
output = tk.Text(root, width = 50, height = 10)
output.config(background = "grey")
output.grid(row = 11, column = 0, columnspan = 2, sticky = "NESW")       





root.mainloop()