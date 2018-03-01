#todo, change to random number
import random

answer = random.randint(0,5)
guess=int(raw_input("enter a number, 0-5:"))


if(guess > answer):
	print("Your number is too high")
	guess = int(raw_input("Enter a number, 0-5:"))
	if(guess > answer):
		print("Your number is still too high")
	elif(guess < answer):
		print("Your number is too low")
	elif(guess == answer):
		print("Good job! you found my number!")
elif(guess < answer):
	print("Your number is too low")
	guess = int(raw_input("Enter a number, 0-5:"))
        if(guess > answer):
                print("Your number is too high")
        elif(guess < answer):
                print("Your number is still too low")
        elif(guess == answer):
                print("Good job! you found my number!")
elif(guess == answer):
	print("Yes, you guessed my number")

