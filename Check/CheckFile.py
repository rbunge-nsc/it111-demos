import re

#Open a file and store the text:
filename = input("Enter a file name:")
f = open(filename, "r")
filetext=""

for x in f:
  filetext+=x

#print(filetext)

#Check if the file contains a specific text:
textinput = input("Enter some text to check for in the file:")
match = re.search(textinput, filetext)

if match:
  print("YES! We have a match!")
else:
  print("No match")
