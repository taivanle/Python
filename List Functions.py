#List Functions
lucky_numbers = [42, 8, 15, 16, 23, 4]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tony"]
#friends.extend(lucky_numbers)
#friends.append("Creed")
#friends.insert(1, "Shrek")
#friends.remove("Tony")
#friends.clear()
#friends.pop()

friends_2 = friends.copy()

#print(friends.index("Kevin"))

#print(friends.count("Jim"))
#friends.sort()
#lucky_numbers.sort()
#lucky_numbers.reverse()

print(friends_2)
#print(lucky_numbers)


#using the .extend function will allow you to grab a list and add more to it
#using .append will allow to ad individual elements to a list, this will naturally add the element to the end of the list
#using .insert will take two parameters, the index where we want to insert the parameter and the name of the elemet  you want to add
#using .remove will allow us to remove elements
#can reset the list using .clear
#using .pop which will pop the last element off of the list
#to see if someone is in the list we can use friends.index("Kevin"), it will show us the index of the searched string. if it is not in the list, we will get an error
#we can also see how many of an elemt are in the list using .count
#we can also sort the list using .sort and it will sort it in ascending order, in this case, alphabetical order. we can also use lucky_numbers to sort in numerical order!
#reversing the list will reverse the order of the list. use .reverse
#we can copy the list using .copy