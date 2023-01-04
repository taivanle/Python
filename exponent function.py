#exponent function

#will allow us to take a certain number and raise it to a specific power

#one way to do this is:

#print(2**3)

#we can also use a for loop to do this for us.
def raise_power_level(base_num, power_num):
    result = 1
    for index in range(power_num): #the range will set the range through a collection of numbers 
        result = result * base_num
    return result

print(raise_power_level(3, 4))
    