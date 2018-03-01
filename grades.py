# Colors
PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
GREY = '\033[90m'
WHITE =	'\033[1m'


grade = float(raw_input("enter grade"))
if(grade >=90.0):
	print(BLUE+"You got an A")
if(grade >= 80.0 and grade < 90.0):
	print(GREEN+"You got a B")
if(grade >= 70.0 and grade < 80.0):
	print(PURPLE+"You got a C")
if(grade >= 60.0 and grade < 70.0):
	print(YELLOW+"You got a D")
if(grade >= 50.0 and grade < 60.0):
        print(RED+"You got a F")
if(grade >= 0.0):
	print(RESET)
if(grade >= 1.0):
        print(WHITE)

