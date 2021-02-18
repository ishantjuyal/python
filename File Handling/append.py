"""
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""

f = open("sample2.txt", "a") # The "a" in mode means append, so it will add content, not overwrite
f.write("I added this to the file!")
f.close()

#open and read the file after the appending:
f = open("sample2.txt", "r")
print(f.read())