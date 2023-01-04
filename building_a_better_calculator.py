#Building a better calculator
#will be able to do all the basic arithmatic functions, add, minus, divide, multiply

num1 = float(input("Enter first number: ")) #using float like this will turn the string into a numerical value.
op = input("Enter operator: ") #op = operator, to find out if they want to add, minus divide or multiply
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")