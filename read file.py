'''
the first thing to read a file is open that file inside the pyhton file. open()

open()  this will either be a relative path to the file, an absolute path to the file.
'''

#import os

#print(os.getcwd())


#s.chdir(default_path) chdir = change directory



#matrix_dir = os.getcwd() + "/learning/matrix.txt"  #getcwd = get current working directory


'''r means only read the information in the file, w means write, a means apend which means you can add information but not edit 
r+ is read and write.
whenever opening a file, you need to close the file.
'''

'''
print(mission_file.readable())
mission_file.close() #will close the file so that we can no longer access it.
'''

'''
we need to check if the file is readable, we can use .readable to see if the file is readable via a boolean value.
to get information from the file we will use the print statement

once we determine that the file is readable we can use the .read function which will spit out all the information from the file
'''
#mission_file = open("matrix.txt", "r")

#print(mission_file.read())
#mission_file.close()

#using .readline will allow us to read  lines of the code.
'''
#mission_file = open("matrix.txt", "r")

print(mission_file.readline()) #will read the first line
print(mission_file.readline()) #will read the second line
mission_file.close
'''

#using .readlines will allow the code to read all our lines but sort them into an array
'''
#mission_file = open("matrix.txt", "r")
print(mission_file.readlines()) #to access specific lines use [] after readlines() and specify which item within the array.
mission_file.close
'''
#we can use a for loop within this by:

mission_file = open("matrix.txt", "r")
for matrix in mission_file.readlines():
    print(matrix)
mission_file.close()

