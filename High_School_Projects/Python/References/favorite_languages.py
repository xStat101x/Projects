favorit_languages = {
    'jan' : 'Python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
print("sarah's favorite language is " +
    favorit_languages['sarah'].title() +
    ".")
for name in favorit_languages.keys():
    print(name.title() + name.title() + ", I see your favorite language is " + favorit_languages[name].title() + "!")


if 'erin' not in favorit_languages.keys():
    print('Erin, please take our poll!')

#Looping dictionary keys in order
for name in sorted(favorit_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#Looping dictionary values in order
print("The following languages have been mentioned:")
for language in set(favorit_languages.values()):
    print(language.title())

favorit_languages = {
    'jan' : ['Python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
}

for name, languages in favorit_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title()) 