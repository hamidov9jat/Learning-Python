guests = ['hfsdah', 'faefa', 'fawoijk']
guests.append("diourwc")
print(guests)
print("\nHere is the sorted list:")
print(sorted(guests))
print(guests)
print()

print("\nHere is the list in reverse alphabetical order:")
print(sorted(guests, reverse=True))
print("\nHere is the original list again:")
print(guests)

print("\nThe lists order has changed:")
guests.reverse()
print(guests)

print("\nThe original list:")
guests.reverse()
print(guests)

print("\nThe original list in alphabetical order (changed permanently):")
guests.sort()
print(guests)

print("\nThe original list in reverse alphabetical order (changed permanently):")
guests.sort(reverse=True)
print(guests)

print(f"\nNumber of invited guests: {len(guests)}")

x = []
print(len(x)) # length of an empty list is 0

# IndexError: list index out of range
# print(x[-1])
# pritn(x[0])

