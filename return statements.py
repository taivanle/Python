#return statements

#using return will bring information back from the function.

def cube(num) :
    return num*num*num # using return here will execute the function and see the return. It will give a value back. 

result = (cube(4))
print(result)#Will give output none

#using return will allow you to return a value back to the caller,whatever is calling the function.


#cannot put code after the return statement! t his is because when we use retunr it will break us out of the function.
#can return any data type, boolean, string, array
