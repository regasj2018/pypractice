def add(a,b):
	c = a + b
	return c

def multiply(a,b):
	c = 0
	for x in range(a):
		c = add(c,b)
	return c

x = add(23,24)
y = add(1,2)
z = multiply(3,4)
print(x,y,z)



def power(a,b):
	c = 1
	for x in range(b):
		print(c)
f = power (2,3)
print(f)
