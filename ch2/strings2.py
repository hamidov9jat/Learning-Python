lang = 'python   '
print(lang.rstrip())
print(lang + 'and three spaces')

lang = lang.rstrip()
print(lang + "\nthere were no spaces")

lang = "   python"
print(lang.lstrip())
print(lang)
lang = lang.lstrip()
print(lang)

lang = '   python   '
print(lang.strip())
print(f'{lang}\nthere were three on both sides\
 of the string above')

message\
=\
'''triple
quotes
	will
span
	multiple lines
without
errors'''

print(message)
