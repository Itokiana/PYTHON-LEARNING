
# PYTHON NUMBERS

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))


# PYTHON LIST
"""
List is an ordered sequence of items. 
It is one of the most used datatype in Python and is very flexible. 
All the items in a list do not need to be of the same type.
"""

a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

# -----------------------------------------------------------------------------

# PYTHON TUPLE
"""
Tuple is an ordered sequence of items same as list.
The only difference is that tuples are immutable. 
Tuples once created cannot be modified.
"""

t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
# t[0] = 10

# -----------------------------------------------------------------------------

# PYTHON STRINGS
"""
String is sequence of Unicode characters. 
We can use single quotes or double quotes to represent strings. 
Multi-line strings can be denoted using triple quotes, ''' or ""'.
"""

s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
# s[5] ='d'

# -----------------------------------------------------------------------------

# PYTHON SET
"""
Set is an unordered collection of unique items. 
Set is defined by values separated by comma inside braces { }. 
Items in a set are not ordered.
"""

a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

# -----------------------------------------------------------------------------

# PYTHON DICTIONNARY
"""
Dictionary is an unordered collection of key-value pairs.
"""

d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1]);

print("d['key'] = ", d['key']);

# Generates error
# print("d[2] = ", d[2]);

# -----------------------------------------------------------------------------

# CONVERSION BETWEEN DATA TYPES
"""
We can convert between different data types 
by using different type conversion functions 
like int(), float(), str() etc.
"""
print(float(5))
print(int(10.6))
print(float('2.5'))
print(str(25))

"""
We can even convert one sequence to another.
"""
print(set([1,2,3])) # => {1, 2, 3}
print(tuple({5,6,7})) # => (5, 6, 7)
print(list('hello')) # => ['h', 'e', 'l', 'l', 'o']

"""
To convert to dictionary, each element must be a pair
"""
print(dict([[1,2],[3,4]])) # => {1: 2, 3: 4}
print(dict([(3,26),(4,44)])) # => {3: 26, 4: 44}