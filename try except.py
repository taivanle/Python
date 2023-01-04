'''
try except block will allow your program to try out a piece of code
for example, below, if you enter a string when an integer is supposed to be used. We can tell the user they entered the wrong thing.
'''


try:
    #value = 10/0 #the except cannot catch this
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: #zerodivisionerror will catch the zero division error. using as err will allow us to store the error.
    #print("Divided by zero")
    print(err)
except ValueError: #valueerror is when you enter the wrong type of information, e.g. we were supposed to input a number, if you input a word that is a ValueError
    print("Invalid input")# if the user enters something that isnt what we expected, it will tell us that there is an invalid input.  