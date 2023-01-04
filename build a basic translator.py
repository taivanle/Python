#build a basic translator


#for this translator, the language is called Top G language, this is where all vowels = g
def translate(phrase): #we want this code to translate the phrase
    translation = ""
    for letter in phrase:
        if letter in "aeiou": #allows us to check if the letter is inside of the string
            if letter.isupper(): #to check if the vowels that it is searching for are uppercase
                translation = translation + "G"
            else:
                translation = translation + "g" #else, they will be replaced with lowercase
                
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))