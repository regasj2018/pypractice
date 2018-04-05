socks = "socks"
jeans = "jeans"
laptop = "laptop"
toiletries = "toiletries"


done = "n"


luggage = []
while(done != "y"):
	item1 = raw_input("what you like to pack?")
	luggage.append(item1)
	item2 = raw_input("what you like to pack?")
	luggage.append(item2)
	item3 = raw_input("what you like to pack?")
	luggage.append(item3)
	done = raw_input("add another item? y/n")
print(luggage)

for item in luggage:
	print(item)


grades = raw_input("enter your grade")

sum = 0

for grade in grades:
	sum = sum + grade
	print(int(sum))
