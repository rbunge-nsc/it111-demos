import os

filename = input("Enter a file name:")
f = open(filename, "x")
print("File name " + filename + " has been created.")
f.close()

save_path = '/tmp/files'
completeName = os.path.join(save_path, filename)
print(completeName)

textinput = input("Enter some text:")
f = open(completeName, "a")
f.write(textinput)
f.close()