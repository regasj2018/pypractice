



secret = 7
number = 0

while(number != secret):
	print("Guess my number between 0 and 10")
	number = int(raw_input(">"))
	if(number < secret):
		print("your number is too low ")
	if(number > secret):
		print("your number is too high")


#loopCount = 0
#index = 10
#while(index > loopCount):
#	print(index)
#	index = index - 1

