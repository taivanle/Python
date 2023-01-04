#Building a basic calculator
#we will get two numbers from a user and print the number in the screen to practice getting information from users as well as using numbers
#create 2 variables and 2 numbers that the user wants to add
#num1, num2 and result are the variables

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
#result = int(num1) + int(num2)
result = float(num1) + float(num2)

print(result)

#will print out the wrong answer so we need to modify the code
#answer is wrong because python will default to turning it a string
#we will need to convert the string to numbers by using int() to turn it into an integer, no decminal point!
#this will give us the correct answer

#this calculator is very limited as we cannot use decimal points. we can use float() to avoid this

