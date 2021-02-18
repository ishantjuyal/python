"""
To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:
"""

f = open("sample.txt", "r")
print(f.read())



"""
Read Only Parts of the File

By default the read() method returns the whole text, 
but you can also specify how many characters you want to return:

Return the 5 first characters of the file:
"""
print("\nReturn the 5 first characters of the file:\n")
f = open("sample.txt", "r")
print(f.read(5))