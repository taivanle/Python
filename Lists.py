#Lists
#when programming in python you will be dealing with large amounts of data
#using lists allow us to organise it and keep track of them a lot easier

#we should first give our list a name
#when using [] it shows python we want to store values in a list
friends = ["Mikko", "Jez", "Fitz", "Rose", "Owen"]

friends[1] = "Yuki"
print(friends[1:4])

#we can access any value within the list
#can put strings, numbers or booleans in the list
#friends = ["Mikko", 25, False]
#using the [] we can find the index of where the strings are and it will only print the string which is in the position stated
#using : after the index position will tell python, grab the data that starts at the stated index AND all the ones after it
#adding a number after the : will tell python, grab all the index's UNTIL the stated index.
#print(friends[1:4]) will print jez, fitz, rose
#using friends[1] will allow us to modify the index at position 1 with whatever we set it equal to
