# It is a good practice to always close the file when you are done with it.

f = open("sample.txt", "r")
print(f.readline())
f.close() # This closes the file