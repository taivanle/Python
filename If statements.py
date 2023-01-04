#If statements
#allows our programmes to respond to the inputs that are given
#for example, if im hungry 
    #i eat breakfast


#example:

#is_tired = False
#if is_tired:
  #  print("You are tired.")
#else:
#    print("Get to coding!")

#to make this more complex:

#is_tired = False
#is_motivated = False

#if is_tired or is_motivated:
 #   print("Go do work then!")
#else:
 #   print("Still do more work!")

#using elif (else if)


is_tired = True
is_motivated = False

if is_tired and is_motivated:
    print("Go do work then!")
elif is_tired and not(is_motivated):
    print("you are motivated, you can do this!")
elif not(is_tired) and is_motivated:
    print("Use that energy to code")
else:
    print("Still do more work!")