"""
HOW TO OPEN FILE?
"""
f = open("test.txt")    # open file in current directory
f = open("C:/Python33/README.txt")  # specifying full path

f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b')

f = open("test.txt",mode = 'r',encoding = 'utf-8')

# -------------------------------------------------------------

"""
HOW TO CLOSE FILE ?
"""

f = open("test.txt",encoding = 'utf-8')
# perform file operations
f.close()


try:
    f = open("test.txt",encoding = 'utf-8')
    # perform file operations
finally:
    f.close()


with open("test.txt",encoding = 'utf-8') as f:
    # perform file operations


# -------------------------------------------------------------

"""
HOW TO WRITE TO FILE WITH PYTHON ?
"""

with open("test.txt",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

# -------------------------------------------------------------

"""
HOW TO READ TO FILE WITH PYTHON ?

>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'
>>> f.read(4)    # read the next 4 data
' is '
>>> f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'
>>> f.read()  # further reading returns empty sting


We can change our current file cursor (position) using the seek() method. 
Similarly, the tell() method returns our current position (in number of bytes).

>>> f.tell()    # get the current file position
56
>>> f.seek(0)   # bring file cursor to initial position
0
>>> print(f.read())  # read the entire file
This is my first file
This file
contains three lines

We can read a file line-by-line using a for loop. 
This is both efficient and fast.

>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines

Alternately, we can use readline() method to read individual lines of a file. 
This method reads a file till the newline, including the newline character.

>>> f.readline()
'This is my first file\n'
>>> f.readline()
'This file\n'
>>> f.readline()
'contains three lines\n'
>>> f.readline()
''

>>> f.readlines()
['This is my first file\n', 'This file\n', 'contains three lines\n']
"""