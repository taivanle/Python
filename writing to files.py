#writing to files

'''
python allows you to read external text files. we can also write a file too and appending on to them!
'''

mission_file = open("matrix.txt", "a") #a allows us to append a file, add text to the end, not edit previous text
print(mission_file.write("I will escape the matrix"))
print(mission_file.write("\nMei is waking up!"))
mission_file.close()

'''
When doing this, you must be careful because you can mess a file up very easily.
you need to ensure that you are starting on the next line.
to add a new line to when appending the text, you nee dto add special code to do this. Will need to do \n

Using w (write) instead of a, it will overide everythhing in that existing file.
we can also use w to create a new file by editing the file name, for example, open("matrix1.txt", "w")
'''
