magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician, end = ' ')
print()

print(magician) # the last value in the list of magicians
print()

for magician in magicians:
#IndentationError: expected an indented block (if there is no identation after
#the for statement)	
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
 #IndentationError: unindent does not match any outer indentation level
 #print("Nice trick!")

 	'''
 	If you accidentally indent code that should run after a loop has finished, that
	code will be repeated once for each item in the list. Sometimes this prompts
	Python to report an error, but often this will result in a logical error.
 	'''
 	#Indenting Unnecessarily After the Loop (Sometimes this prompts Python 
 	#to report an error, but often this will result in a logical error.)
	#print("Thank you, everyone. That was a great magic show!")
print("Thank you, everyone. That was a great magic show!")
	#IndentationError: unexpected indent
	#print("Hello")














