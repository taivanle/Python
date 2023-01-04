#Functions

#a function is basically a collection of coe which performs a certain task
#allow us to organise code better

def say_hi(name): #def shows python we want to use a function, does not need an underscore but can be used. tells python all the code after line 6 will be in that function

    #print("Hello User")#pressing enter will indent the text to show what code lies within the function
    print("Hello " + name)
#print("Top") #this shows that python executes code within the order it is written
say_hi("Mike") #to execute the code in the function we need to call it, this is done by typing the functions name with ()
say_hi("Owen")
#print("Bottom")

#we can make the functions more powerful by giving them information. These are called parameters
#parameters are a piece of information we give to a function. In this case, we are using name in def say_hi
#when the code is called that means we have to give it a name in say_hi()
#instead of using "Hello User" we can use "Hello" + name
# the function can be called multiple times to create multiple outputs. for example say_hi("Owen")
#we can realistically pass as many parameters as we need such as age.

def say_hi(name, age):
    print("Hello " + name + " you are " + age)
say_hi("Mike", "24")
say_hi("Owen", "25")
#notice how we declared the age in say_hi

#if we wanted to write the age as a number we would have to convert the age within the print to be a string as python can only print either strings or numbers or booleans
#within the same print function.

def say_hi(name, age):
    print("Hello " + name + " you are " + str(age))
say_hi("Mike", 24)
say_hi("Owen", 25)