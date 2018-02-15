s=raw_input("type a word")
upper_s = s.upper()
print (upper_s)
lower_s = s.lower()
print(lower_s)

combined = upper_s + lower_s

print(combined)

num_s = len(s)
print(num_s)
num_combined = len(combined)
print(num_combined)


halfway = len(s)/2
print(s[halfway])
print(s[0])
last = len(s) - 1
print(s[last])
print(s[-1])

firsthalf = s[0:halfway]
lasthalf = s[halfway:len(s)]
print(firsthalf)
print(lasthalf)

skip = s[1::2]
print(skip)

value = s[len(s):halfway:-1]
print(value)

print(s.count("1"))


print(s.find("e"))
print(s[:s.find("e")])

replaced = s.replace("great","awesome")
print(replaced)

words = s.split()
numberofwords = len(words)
print(words[0:2])
sentence = "\n".join(words)
print(sentence)
newsentence = sentence.replace("\n",":-)")
print(newsentence)

#to create a random number

import random


x = random.randint(1,10)
print(x)
