kitchen = 23.5
bedroom = 33.0

#and statement 
print(kitchen > 20 and bedroom < 30)

#or statement
print(kitchen > 20 or bedroom < 33)

#not statement
print(not(kitchen < 20, bedroom > 40))


#Conditional statements

height = 45.5 

# IF statement
if height < 50:
	print('you are too short')
	
	#Elif statement 
if height != 40:
	print('When were you birthed?')
elif height < 45.5:
	print('Think again before coming in')
else:
	print(" what do you need ")
	
	#else statement
if height == 50:
	print("you're not fit")
else:
	print('Welcome back')
	
	