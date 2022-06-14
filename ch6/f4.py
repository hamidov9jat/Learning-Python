favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# friends = ['phil', 'sarah']

# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favorite_languages.keys():
#     print("\nErin, please take our poll!\n")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")
#     # print(f"{name.title()},\n thank you for taking the poll.")

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

languages = {'python', 'ruby', 'python', 'c'}
print(languages)
languages = {'python', 'ruby', 'python', }
print(languages)
languages = {'python', 'ruby', 'python', 'c', 'c', }
print(languages)
print()
for language in languages:
    print(f"{language.title()}")

print()
languages = {'python', 'ruby', 'python', 'c'}
for language in languages:
    print(f"{language.title()}")


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'jen': "changed to java"
}
print(favorite_languages)















