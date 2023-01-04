#Working with Numbers
#the math functions in here are the most commonly used for math operations
#when working with numbers we dont need to use ""
print(2)

#can also use decimal and negative numbers
print(-1.234)

#can also be used for basic arithmatics
print(1 + 1)
print(2 - 1)
print(2 * 3)
print(6 / 3)

#can also use numerical symbols to specify order of operations
#will do 3 * 4 first and then + 5 to give us an answer of 17
print(3 * 4 +  5)

#if we wanted to change the order we could use ()
#this would do 4 + 5 and then * 3 to give us an answer of 27
print(3 * (4 + 5))

#there is also % which is a modulus operator
#will do 10 / 3 but will only show us the remainer, in this case it is 1
print(10 % 3)

#can store these numbers within variables.
my_num = 10
print(my_num)

#can convert this into a string using str()
#if you dont use str() then python will throw an error as you cannot print a number and a string together
# without converting the number into a string first
my_num = 10
print(str(my_num) + " is nice and even!")

#A function is a collection of code that does something.
#can give us information

#abs = the absolute value
#will print 10 as 10 is the absolute value of -10
my_num = -10
print(abs(my_num))

#pow allows us to give the function 2 pieces of information
#doing print(pow(10, 2)) is the same as 10^2 so our value should be 100
my_num = 10
print(pow(10, 2))

#can also use another function called max
#will tell us which number out of the two that are inputted is larger in value, and min will do the opposite
my_num = 10
print(max(10, 2))
print(min(10, 2))

#the round function will allow us to round the number to the closest whole number
print(round(3.5))
print(round(3.2))

#in python we can import external code by using from, for example
#very important as it allows us to access a lot more math functions!!!
from math import *
#this will allow us to access more functions

#using floor() will remove the decimal place
print(floor(3.5))

#using ceil() will round the number up no matter what
print(ceil(3.1))

#using sqrt() is square root
print(sqrt(25))
