# You can return one line by using the readline() method:

f = open("sample.txt", "r")
print(f.readline())
print(f.readline())

"""
Writing two times print both the lines separated by a new line. Writing once
would print the first line only
"""

# By looping through the lines of the file, you can read the whole file, line by line:

print("\nLoop here:\n")
f = open("sample.txt", "r")
for x in f:
  print(x)