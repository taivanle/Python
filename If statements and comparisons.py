#If statements and comparisons
#using comparisons inside of our if statements
#def is used to define a function!!!!!

def max_num(num1, num2 ,num3):
    if num1 >= num2 and num1 >= num3:
        return num1 
    elif num2 >=num1 and num2 >=num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

#>= less than or equal to, OR greater than or equal to. basically a boolean using comparisons
# == is equal
# != not equal