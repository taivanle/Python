#Dictionaries
#allows us to store information known as key value pairs
#can call it back by referring it by its key.
 #give dictionary a name

monthConversions = {
"Jan": "January",
"Feb": "February",
"Mar": "March",
 }
 # always use these{} when creating a dictionary
 #"jan" is the key! All keys have to be unique.
print(monthConversions["Jan"])
#can also use
print(monthConversions.get("Aug", "Not a valid key"))
#using .get will allow you to speicify a default value if the key is not found. Therefore you can enter a string which will be the default value of the invalid key.
#In this case it is "Not a valid key"