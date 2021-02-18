"""
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""

f = open("sample3.txt", "w") # The "w" in mode means it will overwrite the content!
f.write("I deleted the content and added this!")
f.close()

#open and read the file after writing:
f = open("sample3.txt", "r")
print(f.read())