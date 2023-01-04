#For loop


#for letter in "Escape the matrix":   #in this for loop, (the letter = variable) will print every single letter and it loops until the string runs out of letters
 #   print(letter)


friends = ["Mikko, Jez, Fitz"]
for friend in friends:   #in this for loop, (the letter = variable) will print every single friend and it loops until the array runs out of friends
    print(friend)


#This can be used for indexes as well.

for index in range(11):
    print(index)
    #In this code, it will only print up to the number 10 as it will exclude the number 11 


#if we re-run this code and we include range(2, 11) it will start at the number 2 and stop at the number 10

for index in range(2, 11):
    print(index)
    
    

friends = ["Mikko, Jez, Fitz"]
for index in range(len(friends)):   #if i wanted to get the length of this array i could use this <--
    print(friends[index])


#there are a lot of things you can do in a for loop. For example

friends = ["Mikko", "Jez", "Fitz"]
for index in range(5):
    if index == 0:
        print("HOWDY")
        print("Hello frens")