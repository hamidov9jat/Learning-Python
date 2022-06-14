a = {'key1': 1, "helk": 2}

print(a)

print(a["helk"])

val1 = a.get("ss")
print(val1)

v = a.get("sk", 78)
print(v)

del a["key1"]
print(a)
a["sjk"] = 89
print(a)

a["sjk"] = 798
print(a)


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#KeyError: 'edw'
# print(a['edw'])

favorite_languages["nick"] = "C++"
print(favorite_languages)

for key in favorite_languages:
    print(f"{key}: {favorite_languages[key]}")
print()
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print()

for name in favorite_languages.keys():
    print(name.title())
print()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!\n")




















