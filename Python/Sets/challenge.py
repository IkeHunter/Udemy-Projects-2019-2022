# My version ----
#
# string = input("Please enter some text: ")
#
# string = set(string)
# print(string)
# vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u", " ", ","}
#
# string.difference_update(vowels)
# print(sorted(string))


# Instructors version ----

sampleText = "Python is a very powerful language"

vowels = frozenset("aeiou")
# vowels = {"a", "e", "i", "o", "u"}
finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)

