story = '''Once upon a time in a place called {0}. There was a {1} princess 
named {3} she lived in a huge {5}. She had many {2} friends, her best friend
was named {6}. They {4} a lot of sports and they {7} every board game in {0}.
One day a {10} {8} {9} {6}. {3} swore it would {11} the {8}.
 
place1 = raw_input("enter a place") 
adjective1 = raw_input("enter a adjective")
name1 = raw_input("enter a name")
verb1 = raw_input("enter a verb")
noun1 = raw_input("enter a noun")
name2 = raw_input("enter a different name")
verb2 = raw_input("enter a verb")
noun2 = raw_input("enter a noun")
verb3 = raw_input("enter a verb")
adjective2 = raw_input("enter a adjective") 
verb4 = raw_input("enter a verb")
adjusted = story.format(place1, adjective1, verb1, name1, noun1, adjective1, name2, verb1, verb2, place1, adjective2, noun2, verb3, name2, name1, verb4, 
noun2)

print(adjusted)
