#Loops are structures used to repeat sections of code. 
#They are useful if you have to do the same thing more than once
#or you can establish a pattern. 

#Example 1: 
print("0")
print("1")
print("2")
print("3")
print("4")
PRINT("**********")

#this is a counted loop I want you to think about 
#count, check, change 
# i = 0, 0 < 5, True - RUN LOOP 
# i = 1. 1 < 5, True - RUN LOOP
# i = 2. 1 < 5, True - RUN LOOP
# i = 3. 1 < 5, True - RUN LOOP
# i = 4. 1 < 5, True - RUN LOOP
# i = 5, 5 = 5, False = EXIT AND MOVE ON 
for i in range (4,11,2):
		#ANYTHING TABBED IS CONSIDERED THE LOOP BLOCK 
		print(i)

print("*********")

for i in range(2,6,1)
	print(i*1)

print("**************BACKWARDS************")
#If you change you increment to go in reverse
#the check is always i > check, in this case -1
For i IN range(10,-1,-1):
	print(i)	

print("MOVING ON")


print ("**********Printning String Characters***")
str = "Monkey"
#We can use the loop to go through each index
#in a string to print out every letter 
#ALWAYS INDICATE THE LENGTH OF A WORD USING THE FUNCTION 
#LEN
for i in range(0,len(str), 1)
	print(str[i])

print("MOVING ON")

print("**********PRINT STRING IN REVERSE***********")
for i in range(len(str) -1, -1  -1): 
		print(str[i])

****************("PRINT EVERY SECOND LETTER IN STR START AT INDEX 0******************")
