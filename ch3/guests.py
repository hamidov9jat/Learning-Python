guests = ['hfsdah', 'faefa', 'fawoijk']
print(f'I want to invite {guests.pop().title()}')

guests.append("diourwc")
print(guests)

cannot = 'faefa'
where_in_the_list = guests.index('faefa')
guests.remove('faefa')
print(guests)
print()
guests.insert(where_in_the_list, 'ljiosie')
print(guests)

guests.insert(0, "NIK".lower())
guests.insert(int(len(guests)/2), "KIm".lower())
guests.append("Jimmy".lower())
print(guests)

guests = ['hfsdah', 'faefa', 'fawoijk']
guests.append("diourwc")

print(f"Sorry can't invite you {guests.pop().title()}")
print(f"Sorry can't invite you {guests.pop().title()}")
print(guests)
print(f"{guests[0].title()} and {guests[1].title()} are still invited")

del guests[-1] # or del guests[0]
del guests[-1] # or del guests[0]

print(guests)