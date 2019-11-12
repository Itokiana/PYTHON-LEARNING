
# PYTHON OUTPUT USING print() function

print('This sentence is output to the screen')
# Output: This sentence is output to the screen

a = 5

print('The value of a is', a)
# Output: The value of a is 5


print(1,2,3,4)
# Output: 1 2 3 4

# print(1,2,3,4,sep='*')
# Output: 1*2*3*4

# print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&


x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))

print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread

print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

#------------------------------------------------------------------------------

# PYTHON INPUT

num = input('Enter a number: ')
print(eval('2+3'))

#------------------------------------------------------------------------------

# PYTHON IMPORT
import math
print(math.pi)

from math import pi
print(pi)

import sys
print(sys.path)