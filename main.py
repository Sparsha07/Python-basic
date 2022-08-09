# open mytext.txt file in read mode
#file1 = open("sparsha.txt", "r")

# Read all contents of text file in a string s

#s = file1.read()

# show the contents from string s

#print(s)

# close the text file
#file1.close()

#with open("sparsha.txt",'w',encoding = 'utf-8') as f:
  # f.write("my first file\n")
   #f.write("This file\n\n")
  # f.write("contains three lines\n")
# Python program to count number of vowels,
# newlines and character in textfile

#def counting(filename):
	

	#txt_file = open(filename, "r")


	#vowel = 0
	#line = 0
	#character = 0


	#vowels_list = ['a', 'e', 'i', 'o', 'u',
	#			'A', 'E', 'I', 'O', 'U']


	#for alpha in txt_file.read():
		

	#	if alpha in vowels_list:
	#		vowel += 1
			
		
#		elif alpha not in vowels_list and alpha != "\n":
#			character += 1
			
		
#		elif alpha == "\n":
#			line += 1


#	print("Number of vowels in ", filename, " = ", vowel)
#	print("New Lines in ", filename, " = ", line)
#	print("Number of characters in ", filename, " = ", character)


#counting('Myfile.txt')

# (a,b) = (6,0)
# try:# simple use of try-except block for handling errors
#     g = a/b
# except ZeroDivisionError:
#     print ("This is a DIVIDED BY ZERO error")

# Creating a List with
# the use of multiple values
# List = ["Supriya",  "Shetty"]
# print("\nList containing multiple values: ")
# print(List)


# List2 = [['Sparsha', 'L], ['Shetty']]
# print("\nMulti-Dimensional List: ")
# print(List2)


# print("Accessing element from the list")
#create a vector
from numpy import array
vec = array([1, 5, 6])
print(vec)
