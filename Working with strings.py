#COMMON STIRNGS THAT ARE USED WITHIN PYTHON, there are more functions!

#strings are plain text, be sure to use ""
print("I'm coding")

#to print 1 string but on two seperate lines use \n
print("I will be hired\nBelieve it!")

#to add a quotation mark within the string use \"
print("how're\"you")

#to add a \ to the text simply use \ be sure to use a capital letter after otherwise it will think you're trying to invoke the shortcut.
print("Fine\And you?")

#string variable - use the variable phrase to print a string in the print()
phrase = "I love fried chicken"
print(phrase)

#concatenation process of getting a string and putting another string on to it.
print(phrase + " it's yummy!")

#to convert the string to lowercase use: phrase.lower()
print(phrase.lower())

#to convert the string to uppercase use: phrase.upper()
print(phrase.upper())

#can also check to see if the string is entirely upper or lowercase by using is
print(phrase.isupper())

#can use  these together
print(phrase.lower().islower())
#will print true as the phrase.lower will turn everything lowercase

#to get the length of the string use len
print(len(phrase))

#can get individual characters from a string using [], with 0 being the first character!
#spaces are included as characters!
print(phrase[0])

#To find the numerical place of the character within the string use .index(). This is called passing a parameter
#a value given to a function is a parameter
print(phrase.index("l"))
# phrase = I love fried chicken

#using .index can also tell us where a word within the string starts, if you input a character that is not in the string asn error will occur
print(phrase.index("fried"))

#using .replace will uses two parameters. first is the one you wish to replace and second is what you want to replace it with.
print(phrase.replace("love", "hate"))
